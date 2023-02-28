from flask import Flask, render_template, jsonify

app = Flask(__name__)
Jobs = [{
  'id': 1,
  'title': 'Data Scientist',
  'salary': '$1500000',
  'location': 'San Fransisco,USA',
}, {
  'id': 2,
  'title': 'Data Engineer',
  'salary': '$160000',
  'location': 'Los Angles,USA',
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'salary': '$1200000',
  'location': 'Bengluru, India',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'salary': '$170000',
  'location': 'Delhi,India',
}, {
  'id': 5,
  'title': 'Full Stack Developer',
  'salary': '$150000000',
  'location': 'Miami,USA',
}, {
  'id': 6,
  'title': 'Data Analyst',
  'location': 'Remote',
}]


@app.route("/")
def Topfreeskill():
  return render_template('home.html', jobs=Jobs)


@app.route("/api/jobs")
def joblist():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
