from flask import Flask,redirect,render_template,request,jsonify
import requests,json



app = Flask(__name__)


@app.route('/' ,methods=["GET"])
def home():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s")
    ml=db.json()
    print(len(ml))
    for i in ml:
        nm=i
        pass
    meals=ml[nm]
    for i in range(len(meals)):
        samplemeal=meals[i]
        break
    return render_template('temp1.html')


@app.route('/firstletter',methods=["POST","GET"])
def firstletter():
    fl=request.form.get()
    return render_template("lstfirstletter.html",letter=fl)


@app.route('/sample',methods=["POST","GET"])
def sample():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s")
    ml=db.json()
    for i in ml:
        nm=i
        pass
    meals=ml[nm]
    for i in range(len(meals)):
        samplemeal=meals[i]
        break
    return render_template("readsample.html",sm=samplemeal)


@app.route('/allmeals')
def allmeals():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s")
    ml=db.json()
    for i in ml:
        nm=i
        break
    meals=ml[nm]
    return render_template("allmeals.html",am=meals)

@app.route('/randommeal',methods=["POST","GET"])
def randommeal():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/random.php?r")
    ml=db.json()
    for i in ml:
        nm=i
        break
    meals=ml[nm]
    return render_template("srradmeals.html",rms=meals)


@app.route('/srbyname',methods=["POST","GET"])
def srbyname():
    dbnm="https://www.themealdb.com/api/json/v1/1/search.php?s="
    print(type(dbnm))
    srnm=request.form.get('Name')
    dbnm=dbnm + srnm
    print(dbnm)
    db=requests.get(dbnm)
    ml=db.json()
    for i in ml:
        nm=i
        break
    meals=ml[nm]
    return render_template("srname.html",srnm=meals)

@app.route('/srbyfltr',methods=["POST","GET"])
def srbyfltr():
    dbnm="https://www.themealdb.com/api/json/v1/1/search.php?f="
    print(type(dbnm))
    srnm=request.form.get('Name')
    dbnm=dbnm + srnm
    print(dbnm)
    db=requests.get(dbnm)
    ml=db.json()
    for i in ml:
        nm=i
        break
    meals=ml[nm]
    return render_template("srname.html",srnm=meals)

@app.route('/srbyid',methods=["POST","GET"])
def srbyid():
    dbid="https://www.themealdb.com/api/json/v1/1/lookup.php?i="
    print(type(dbid))
    srnm=request.form.get('Name')
    dbnm=dbid + srnm
    print(dbnm)
    db=requests.get(dbnm)
    ml=db.json()
    for i in ml:
        nm=i
        break
    meals=ml[nm]
    return render_template("srname.html",srnm=meals)



@app.route('/srre',methods=["POST","GET"])
def srre():
    return render_template("searchbyname.html")


@app.route('/mealcg',methods=["POST","GET"])
def mealcg():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
    cg=db.json()
    for i in cg:
        nm=i
        break
    category=cg[nm]
    print(category)
    for i in range(len(category)):
        for k in category[i]:
            print(k)
        break
    return render_template("mealcategory.html",cgs=category)


@app.route('/Listcat',methods=["POST","GET"])
def Listcat():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
    lsc=db.json()
    for i in lsc:
        ct=i
        break
    lstcat=lsc[ct]
    return render_template("category.html",lsct=lstcat)

@app.route('/Listarea',methods=["POST","GET"])
def Listarea():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
    lsa=db.json()
    for i in lsa:
        ct=i
        break
    lstarea=lsa[ct]
    return render_template("area.html",lsar=lstarea)

@app.route('/Listingredients',methods=["POST","GET"])
def Listingredients():
    db=requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
    lsi=db.json()
    for i in lsi:
        ct=i
        break
    lstint=lsi[ct]
    for i in range(len(lstint)):
        for k in lstint[i]:
            print(k)
        break
    return render_template("ingredients.html",lsin=lstint)

@app.route('/ftrcat',methods=["POST","GET"])
def ftrcat():
    dbnm="https://www.themealdb.com/api/json/v1/1/filter.php?c="
    ftnm=request.form.get('Name')
    ml=dbnm + ftnm
    db=requests.get(ml)
    ftct=db.json()
    for i in ftct:
        ct=i
        break
    ftrcat=ftct[ct]
    return render_template("filtercmn.html",ftr=ftrcat)

@app.route('/ftrarea',methods=["POST","GET"])
def ftrarea():
    dbnm="https://www.themealdb.com/api/json/v1/1/filter.php?a="
    ftnm=request.form.get('Name')
    ml=dbnm + ftnm
    db=requests.get(ml)
    ftar=db.json()
    for i in ftar:
        ct=i
        break
    ftrarea=ftar[ct]
    return render_template("filtercmn.html",ftr=ftrarea)


@app.route('/ftrint',methods=["POST","GET"])
def ftrint():
    dbnm="https://www.themealdb.com/api/json/v1/1/filter.php?i="
    ftnm=request.form.get('Name')
    ml=dbnm + ftnm
    db=requests.get(ml)
    fti=db.json()
    for i in fti:
        ct=i
        break
    ftrint=fti[ct]
    return render_template("filtercmn.html",ftr=ftrint)


@app.route('/srreftr',methods=["POST","GET"])
def srreftr():
    return render_template("filter.html")

if __name__=='__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
