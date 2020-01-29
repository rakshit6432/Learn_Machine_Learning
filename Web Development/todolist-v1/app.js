const express = require("express");
const bodyParser = require("body-parser");
const dateModule = require(__dirname + "/date.js");

const app = express();
const items = ["food1", "food2", "food3"];
const workItems = []

app.set('view engine', 'ejs');


app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));


app.get("/", function(req, res) {

  const date = dateModule.getData();

  res.render("list", {
    listTitle: date,
    newListItems: items
  });
});


app.post("/", function(req, res) {
  const item = req.body.newItem;

  if (req.body.list == "Work") {
    workItems.push(item);
    res.redirect("/work");
  } else {
    items.push(item);
    res.redirect("/");
  }
});


app.get("/work", function(req, res) {
  res.render("list", {
    listTitle: "Work List",
    newListItems: workItems
  });
});


app.post("/work", function() {
  const item = req.body.newListItem;
  workItems.push(item);
  res.redirect("/work");
});


app.listen(3000, function() {
  console.log("Port running at 3000");
});
