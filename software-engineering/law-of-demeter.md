# Law of Demeter

Methods can only send messages to:

* their own object (e.g. `this` or `self`)
* their own object's attributes (e.g. `this.reporter`)
* their arguments
* objects they create
* global variables
