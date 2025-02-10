from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pengajuan')
def pengajuan():
    return render_template('pengajuan.html')

@app.route('/persetujuan')
def persetujuan():
    return render_template('persetujuan.html')

@app.route('/riwayat')
def riwayat():
    return render_template('riwayat.html')

if __name__ == '__main__':
    app.run(debug=True)
