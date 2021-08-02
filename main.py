from flask import Flask,jsonify,request
import csv
import pandas as pd

all_movies = []
liked_movies = []
not_liked_movies = []
did_not_watch = []


with open('movies.csv') as f:
    reader = csv.reader(f)
    #file_data = list(reader)
    #all_movies = reader[1:]
    for i in reader:
        all_movies.append(i)


#print(all)

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        data:all_movies[0],
        status:"success"
    })


@app.route("/liked-movie",methods = ["POST"])
def liked_movie():

    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)

    return jsonify({
        status:'success'
    }),201


@app.route("/unliked-movie",methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)

    return jsonify({
        status:"success"
    }),201


@app.route("/did_not_watch-movie",methods=["POST"])
def did_not_watch_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch_movies.append(movie)

    return jsonify({
        status:"success"
    }),201

if __name__ == "__main__":
    app.run()


