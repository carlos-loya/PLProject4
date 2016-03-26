
"use strict"; 
//function application
var list = function() { //function application
    var list = function () { //will create a closure
        function Node(data) { //named function called Node that takes one argument
            this.data = data;
            this.next = null;
        }

        var l = { //l is an object
            //declaring variables
            length: 0,
            currentNode: null,
            head: new Node(null),
            ite: null, //added to keep track of the iterator's current node.
            add: function(e) {
                if (l.currentNode === null) {
                    l.head.data = e;
                    l.currentNode = new Node(null);
                    l.head.next = l.currentNode;
                    l.length++;
                    l.ite = l.head;
                }
                else {
                    l.currentNode.data = e;
                    var node = new Node(null);
                    l.currentNode.next = node;
                    l.currentNode = node;
                    l.length++;
                }
            },
        }; //l is part of the environment of closure

        var F = function () { //creating a new object, no prototype, and wont inherit anything
        };
        var f = new F();


        // public data with methods. and all of these methods are visible and are part of the closure
        f.run = function (e) {
            return l[e]; //allows people to see into the closure
        };
        f.first = f.car = function () {
            return l.head.data
        }
        f.rest = f.cdr = function () {
            if(l.length > 0) {
                l.head = l.head.next;
                l.length--;
            }
            return this;
        }
        f.concat = f.cons = function(e){
            if (typeof e === 'string' || e instanceof String) {
            	l.add(e);
            }
            else {
                var n = e.run('head')
                document.writeln(e.run('length'))
                for(var i = 0; i < e.run('length'); i++) {
                    l.add(n.data);
                    n = n.next;
                }
            }
        }
        f.length = function(){
            return l.length
        }

        f.interator = function(){
            //checks if there is data on the current item on the iterator
        	if (l.ite.data != null){
                //assigns current list to a new variable
        		var n = l.ite;
                //assigns the next iterator item to ite
        		l.ite = l.ite.next;
                //returns the data of the new variable
        		return n.data;
        		
        	}else{
                return "";
            }

        }

        f.map = function (f) { //
            if (f instanceof Function){ //check if its a function
                var n = l.head; //the head of the internal list
                for(var i =0; i < l.length; i++){
                    n.data = f(n.data); //this is the function beein passed at the method
                    n = n.next;
                }
            }

        }

        return f;
    }();
    return list; //the list is the whole closure with all its methods
};

var test = new list();
test.concat('1' + "<BR>");
test.concat('2' + "<BR>");
test.concat('3' + "<BR>");
test.concat('4' + "<BR>");
test.concat('5' + "<BR>");
test.concat('6' + "<BR>");
document.writeln(test.interator());
document.writeln(test.interator());
document.writeln(test.interator());
test.concat('inmiddle' + "<BR>");
document.writeln(test.interator());
document.writeln(test.interator());
document.writeln(test.interator());
test.concat('fsdgasd' + "<BR>");
test.concat('sd' + "<BR>");
test.concat('sdd' + "<BR>");
document.writeln(test.interator());
document.writeln(test.interator());
document.writeln(test.interator());
document.writeln(test.interator());
document.writeln(test.interator());

