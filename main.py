from flask import Flask, render_template, request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/7802bc21fa8b2ad3dac2").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["username"])
        print(data["emailid"])
        print(data["phonenumber"])
        print(data["message"])
        list2 = []
        list1 = ['ariswin.jjj@gmail.com']
        my_email = "ariswin.jj@gmail.com"
        password = "hanw hjnt qonq klve"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=list1,
                            msg=f"Subject:Blog contact form\n\n{data}")
        connection.close()
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)