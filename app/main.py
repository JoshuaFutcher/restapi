from flask import Flask
from flask import request, abort, make_response

app = Flask(__name__)

pokemon = {
  1: {
    "name": "Poketomonstor",
    "type": "fire",
  },
  2: {
    "name": "Owomon",
    "type": "water",
  }
}

@app.errorhandler(404)
def not_found(error):
  return 'Not found...'

# CREATE
# ----------------------
@app.route('/', methods=["POST"])
def createPokemon():
  newPokemon = request.get_json()

  pokemon[len(pokemon) + 1] = newPokemon
  return make_response("success", 201)


# READ
# ----------------------

# Get all
@app.route('/', methods=["GET"])
def getAll():
  return pokemon

# Get single
@app.route('/<int:id>', methods=["GET"])
def getById(id):
  return pokemon[id]

@app.route('/<int:id>', methods=["PUT"])
def updateById(id):
  updatePokemon = request.get_json()
  
  pokemon[id].update(updatePokemon)
  return make_response("success", 201)

@app.route('/<int:id>', methods=["DELETE"])
def deleteById(id):
  pokemon.pop(id)
  return make_response("success", 200)