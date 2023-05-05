import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, make_response
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)
app.secret_key = 'mysecretkey'

load_dotenv("./local.env")

testData = "not set"
myDict = {}
plotNames = ["Temperature", "PH", "Distilled_Oxygen", "Pressure"]

# Database Credentials (environment variables)
postgreUser = os.getenv('POSTGRES_USER')
postgreHost = os.getenv('POSTGRES_HOST')
postgreDB = os.getenv('POSTGRES_DB')
postgrePwd = os.getenv('POSTGRES_PASSWORD')


def get_db_connection():
    conn = psycopg2.connect(
        host=postgreHost,
        database=postgreDB,
        user=postgreUser,
        password=postgrePwd
    )
    return conn


def create_plot(data, plot_name):
    fig, ax = plt.subplots()
    print(data['time'])
    ax.plot(data['time'], data['value'])
    ax.set_xlabel('Time')
    ax.set_ylabel(plot_name.split()[0])
    ax.set_title('Your Timeseries Plot for ' + plot_name)
    fig.savefig('static/images/' + plot_name + '.png')


def load_data():
    global myDict
    conn = get_db_connection()
    temp_query = "SELECT * FROM \"CM_HAM_DO_AI1/Temp_value\""
    ph_query = "SELECT * FROM \"CM_HAM_PH_AI1/pH_value\""
    do_query = "SELECT * FROM \"CM_PID_DO/Process_DO\""
    pressure_query = "SELECT * FROM \"CM_PRESSURE/Output\""

    temp_df = pd.read_sql(temp_query, conn)
    ph_df = pd.read_sql(ph_query, conn)
    do_df = pd.read_sql(do_query, conn)
    pressure_df = pd.read_sql(pressure_query, conn)

    myDict = {
        plotNames[0]: temp_df,
        plotNames[1]: ph_df,
        plotNames[2]: do_df,
        plotNames[3]: pressure_df
    }

    create_plot(temp_df, plotNames[0])
    create_plot(ph_df, plotNames[1])
    create_plot(do_df, plotNames[2])
    create_plot(pressure_df, plotNames[3])

    conn.close()


@app.route('/')
def index():
    load_data()
    return render_template(
        'index.html',
        tempPlot=plotNames[0],
        phPlot=plotNames[1],
        doPlot=plotNames[2],
        pressPlot=plotNames[3]
    )


def format_date(start_time, end_time):
    s = "Wed, 19 Apr 2023 " + start_time + ":00 GMT"
    e = "Wed, 19 Apr 2023 " + end_time + ":00 GMT"
    datetime_start = pd.to_datetime(s)
    start = datetime_start.to_datetime64()
    datetime_end = pd.to_datetime(e)
    end = datetime_end.to_datetime64()
    return start, end


@app.route('/filter', methods=["GET"])
def filter():
    global myDict
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    curr_name = request.args.get('current_table')
    df = myDict[curr_name]
    start, end = format_date(start_time, end_time)
    df = df[(df["time"] >= start) & (df["time"] <= end)]
    table_name = curr_name+" from "+start_time+" to "+end_time
    create_plot(df, table_name)
    return jsonify({'START': start_time, 'END': end_time, 'TABLE_NAME': table_name})


@app.route('/download-csv')
def download_csv():
    # create a sample DataFrame
    global myDict
    table_name = request.args.get('current_table')
    # mydata = session.get('mydata', 'No data found.')
    df = myDict[table_name]
    # df = pd.read_csv(pd.compat.StringIO(df_str))

    # convert the DataFrame to a CSV file
    csv_string = df.to_csv()

    # create a response object with the CSV file as its data
    resp = make_response(csv_string)
    resp.headers["Content-Disposition"] = "attachment; filename=" + \
        table_name+".csv"
    resp.headers["Content-Type"] = "text/csv"

    return resp


@app.route("/refresh-data")
def refresh_data():
    load_data()
    return jsonify({'Data Loaded': "success"})


#     return
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
