// Interview questions


// --- Strings --- //

// Check a string to see if it contains only unqiue characters
function stringUnique(string) {
    string = string.toLowerCase();
    var chars = [];
    for (var i=0; i < string.length; i++) {
        if (chars.indexOf(string[i]) !== -1) {
            return false;
        } else {
            chars.push(string[i]);
        }
    } return true;

}

// Reverse a string
// Note: this cannot be done in place, as JS strings are immutable
function stringReverse(string) {
    // This works, but goes FUBAR when given crazy Unicode
    return string.split("").reverse().join("");
}




// Results
console.log(stringUnique('Ace')); // true
console.log(stringReverse('Boom')); // mooB
