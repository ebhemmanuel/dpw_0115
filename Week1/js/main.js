/*

	By Emmanuel Barreto
	Jan 6 2015
	Lab 1 Madlib

*/
// Simple spacer.
console.log('');
// Prompt username.
user 				= prompt('Your name: ');
// Prompt for a second user.
secondUser = prompt('Your bestfriends name: ');
// Prompt for a year. All these prompts will be placed into the loop.
year        = prompt('What year is it!? ');
// Prompt agaaaain.
fridge      = prompt('How many times do you open your fridge a day?');
// An array that will be pushed into the loop through a story.
word       = ["kiked", "sold", "chopped", "Nope."];

function plot(s1,s2){
	return s1 + " " + s2
}
// End of the loop will play this out.
ending = plot("The","End");

/*
Here we'll have an array of 4 items, in this case
we'll use the array to go through the story with a loop.
*/

var i = 0 ;

chapters = ['When'+''+user+'was young, he tried to leave behind his past.
Instead, '+secondUser+' helped '+user+' understand his life. Believe it or not, '+user
+' turned his life upside down very quickly... again. So it was up to '+secondUser
+', to save our world. The year was '+year+', and'+secondUser+' had already'+];





