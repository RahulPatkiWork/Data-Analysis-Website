from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_selection import RFE     #Recursive Feature Elimination
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cervical_cancer")
def cervical_cancer():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/cervical_cancer.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]] = df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 6)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])
        else:
            df.drop(df.columns[i],axis=1)


    # STATS
    stat = df.describe()  # shows stats of per column
    correlation = df.corr()  # shows co-relation between each pir of attributes


    #PREDICTION
    X = df[labels]
    lm = linear_model.LinearRegression()
    model = lm.fit(X, Y)
    predictions = lm.predict(X)
    for i in range(0,len(predictions)):
        if(predictions[i]>=0.5):
            predictions[i]=1
        else:
            predictions[i]=0

    print(predictions[0:10])

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histcer.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scatcer.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/cervical_cancer.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


@app.route("/iris_data")
def iris_data():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/iris_data.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]]= df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 4)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])


    #STATS
    stat=df.describe()     #shows stats of per colomn
    correlation=df.corr()  # shows co-relation between each pir of attributes

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histiri.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scatiri.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/iris_data.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


@app.route("/winequality_red")
def winequality_red():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/winequality_red.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]]= df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 6)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])


    #STATS
    stat=df.describe()     #shows stats of per colomn
    correlation=df.corr()  # shows co-relation between each pir of attributes

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histred.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scatred.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/winequality_red.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


@app.route("/winequality_white")
def winequality_white():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/winequality_white.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]]= df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 6)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])


    #STATS
    stat=df.describe()     #shows stats of per colomn
    correlation=df.corr()  # shows co-relation between each pir of attributes

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histwhi.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scatwhi.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/winequality_white.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


@app.route("/breast_cancer_wisconsin")
def breast_cancer_winconsin():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/breast_cancer_wisconsin.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]]= df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 6)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])


    #STATS
    stat=df.describe()     #shows stats of per colomn
    correlation=df.corr()  # shows co-relation between each pir of attributes

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histbre.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scatbre.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/breast_cancer_wisconsin.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


@app.route("/hepatatis")
def hepatatis():
    df = pd.read_csv('C:/Users/ RahulPatki/Desktop/Datasets/hepatatis.csv', na_values=['?'])
    nanList = df.columns[df.isnull().any()].tolist()
    for i in range(len(nanList)):
        df[nanList[i]]= df[nanList[i]].fillna(df[nanList[i]].mean())

    #FEATURE EXTRACTION
    values = df.values
    X = values[:, 0:df.shape[1] - 1]  # contains values for attributes
    Y = values[:, df.shape[1] - 1]    # contains values for class variable
    model = LogisticRegression()
    rfe = RFE(model, 6)
    fit = rfe.fit(X, Y)
    selectedFeatures = fit.support_


    # GRAPHS
    labels=[]
    valuesmax=[]
    valuesmin=[]
    valuesavg=[]
    for i in range(0,len(selectedFeatures)):
        if(selectedFeatures[i]==True):
            val=values[:,i]
            valuesmax.append(max(val))
            valuesmin.append(min(val))
            valuesavg.append(val.mean())
            labels.append(df.columns[i])

    # PREDICTION
    X = df[labels]
    lm = linear_model.LinearRegression()
    model = lm.fit(X, Y)
    predictions = lm.predict(X)
    for i in range(0, len(predictions)):
        if (predictions[i] >= 0.5):
            predictions[i] = 1
        else:
            predictions[i] = 0

    print(predictions[0:10])


    #STATS
    stat=df.describe()     #shows stats of per column
    correlation=df.corr()  # shows co-relation between each pir of attributes

    df.hist()  # histogram
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(30, 30)
    fig.savefig('static/histhep.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    scatter_matrix(df)  # scatter matrix
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig('static/scathep.png', dpi=100)
    fig.set_size_inches(20, 20, forward=True)

    return render_template("files/hepatatis.html",
                           dataset=df,
                           statobj=stat,correlationobj=correlation,
                           labels=labels,valuesmax=valuesmax,valuesmin=valuesmin,valuesavg=valuesavg)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4555,debug=True)

