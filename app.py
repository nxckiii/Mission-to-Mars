@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

   .update_one(query_parameter, {"$set": data}, options)

   if __name__ == "__main__":
   app.run()