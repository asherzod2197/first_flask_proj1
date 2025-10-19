from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/feature')
def feature():
    return render_template('feature.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')



@app.route('/error404')
def error404():
    return render_template('404.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')










if __name__ == '__main__':
    app.run(debug= True)