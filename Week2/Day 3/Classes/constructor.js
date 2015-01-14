var Employee = (function(){

	function Employee(n){
		this.name=n;
	}
	Employee.prototype.fired = function(){
		console.log("you are fired!! ", this.name);
	};
	return Employee
})();

var newPerson1 = new Employee("Bob");
var newPerson1 = new Employee("Joe");