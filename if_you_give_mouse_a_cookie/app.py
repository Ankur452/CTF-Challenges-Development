from flask import Flask, render_template, request, redirect, url_for, flash, make_response
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome", code = 302)

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    resp = make_response(render_template("index.html"))
    resp.set_cookie('is_admin','True', max_age=60*60*24*365*2)
    resp.set_cookie('utag','hhhg1jg312g3j12f3j1g4kj25gj235khgh43tkkn34y84g8gb483ut32g3bjy98kn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th43hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4jbvejhg8743t782tiurgkjsfhg98iuwh346t32hj412k', max_age=60*60*24*365*2)
    resp.set_cookie('uid','ajdhewiuy98hij43bjy983hfyfew79gsdkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4kjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4lkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th438h3', max_age=60*60*24*365*2)
    resp.set_cookie('Nautilas_CSRF_Token','8tgh73gh74g4npurh8gh3t8ureg9gverg98hjrkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th44hg98hkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th43g9843g98h34g9839gh9436ghiuhfdkguq3209tukerjgh948ghoegh9opo4u3gih43g93', max_age=60*60*24*365*2)
    
    resp.set_cookie('is_cookie_provided','True', max_age=60*60*24*365*2, secure='True')
    
    resp.set_cookie('utag-v1','hhhg1jg312oiberhwoikn34y84g8gb483ut32g3bjy983hfyfevw79gsdlkkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4jfoiwf98732dshf82r9whef98u2fih28fo29ub349th4eaovien3958g3j12f3j1g4kj25gj235khgh43tkjbvejhg8743t782tiurgkjsfhg98iuwh346t32hj412k', max_age=60*60*24*365*2)
    resp.set_cookie('uid-vi','ajdhewiuy98hij4vlkn34y84g8gb483utkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th432g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th438h3', max_age=60*60*24*365*2)
    resp.set_cookie('Apigee_CSRF_Token','8tgh73g3g4554h54hj5356jhrt5h45356hh74g4npurh8gh3t8ureg9gvergkn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th498hjr4hg98h3g9843g98h34g9839gh9436ghiuhfdkguq3209tukerjgh948ghoegh9opo4u3gih43g93', max_age=60*60*24*365*2)
    
    resp.set_cookie('to_mouse','False', max_age=60*60*24*365*2, secure='True')
    
    resp.set_cookie('utag-v2','hhhg1jg312g3j8v7g47v8b3872vb812f3j1kn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4g4kj25gj235khgh43tkjbvejhg8743t782tiurgkjsfhg98iuwh346t32hj412k', max_age=60*60*24*365*2)
    resp.set_cookie('Gateway_CSRF_Token','8tgh73gh74g4n,i3245b984h974hb78478gh7bq4hg2279h97bh425b98b4h59purh8gh3t8ureg9gvekn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th4rg98hjr4hg98h3g9843g98h34g9839gh9436ghiuhfdkguq3209tukerjgh948ghoegh9opo4u3gih43g93', max_age=60*60*24*365*2)
    resp.set_cookie('btag','hhhg1n5387hb8wtb478bw9hw93ebj89r0ajhw0ma-kwkn34y84g8gb483ut32g3bjy983hfyft32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th443j-e=w-,34h-0wjh708gah8u5jg312g3j12f3j1g4kj25gj235khgh43tkjbvejhg8743t78kn34y84ew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th443j-e=w-,34h-0wjh708gah8u5jg312g3j12f3j1g4kj25gj235khgh43tkjbvejhg8743t78kn34y84g8gb483ut32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th42tiurgkjsfhg98iuwh346t32hj412k', max_age=60*60*24*365*2)
    resp.set_cookie('vid','ajdhewiuy98hij43bjy983hfyfew79gsdlkjfoiwf98732dshf82iv9w84hg9t32g3bjy983hfyfew79gsdlkjfoiwf98732dshf82r9whef98u2fih28fo29ub349th443j-e=w-,34h-0wjh708gah8u5jg312g3j12f3j1g4kj25gj235khgh43tkjbvejhg8743t78kn34y84hq3gw78h3rig9e0shj90heqhg8gqw47rf3y:gubg8sebg84gb78gs4br9whef98u2fih28fo29ub349th438h3', max_age=60*60*24*365*2)

    return resp

# @app.route('/login', methods=['POST'])
# def login():
#     # value = request.cookies.get('mouse')
#     if request.method == 'POST':
#         cookie_value = request.form['cookie-name']

#         if cookie_value == "mouse":
#             return redirect("/cookie-received", code = 302)
#         else:
#             return redirect("/", code = 302)
#     else:
#         return redirect("/", code = 302)
        
@app.route('/cookie-received')
def cookie_received():
    return render_template("cookie-received.html", title = 'Cookie-received')

@app.route('/q2wase4rdzxft6ygvbht4', methods=['POST'])
def flag():

    if request.method == 'POST':
        access_token = request.form['acces-token']

        if access_token == "Seriously! You are this Smart. Kudos!!!":
            return render_template("flag.html", title = 'Flag')
        else:
            return redirect("/cookie-received", code = 302)
    else:
        return redirect("/", code = 302)

if __name__ == '__main__':
   app.run()


# Seriously! You are this Smart. Kudos!!!
# VlRKV2VXRlhPVEZqTW5nMVNWTkNXbUl6VldkWldFcHNTVWhTYjJGWVRXZFZNakZvWTI1UmRVbEZkREZhUnpsNlNWTkZhQT09