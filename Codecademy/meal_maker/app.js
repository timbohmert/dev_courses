/* GOAL (provided by Codecademy) As a frequent diner, you love trying out new restaurants and experimenting with different foods. However, having to figure out what you want to order can be a time-consuming ordeal if the menu is big, and you want an easier way to be able to figure out what you are going to eat.

In this project, you’ll use JavaScript to randomly create a three-course meal based on what is available on a menu. We’ll keep running it until we’re satisfied with the generated meal! */

//menu object

const menu = {
   _courses: {
       appetizers: [],
       mains: [],
       desserts: []
   },
   //getter and setter methods for appetizers, mains, and desserts properties within _courses
   get appetizers() {
       return this._courses.appetizers;
   },
   get mains() {
       return this._courses.mains;
   },
   get desserts() {
       return this._courses.desserts;
   },
   set appetizers(appetizerIn) {
       this._courses.appetizers = appetizerIn;
   },
   set mains(mainIn) {
       this._courses.mains = mainIn;
   },
   set desserts(dessertIn) {
       this._courses.desserts = dessertIn;
   },

   //getter method for _courses
   get courses() {
       return this._courses;
   },

   //method for pushing new dishes into course array
   addDishToCourse (courseName, dishName, dishPrice) {
       const dish = {
           dish: dishName,
           price: dishPrice
       };
       this[courseName].push(dish);
   },
   
   //method for getting random dish from course array
   getRandomDishFromCourse(courseName) {
       const dishes = this[courseName];
       const randIdx = Math.floor(Math.random() * dishes.length);
       return dishes[randIdx];
   },

   //method for generating random menu with courses of appetizer, main, and dessert
   generateRandomMeal() {
       const appetizer = this.getRandomDishFromCourse('appetizers');
       const main = this.getRandomDishFromCourse('mains');
       const dessert = this.getRandomDishFromCourse('desserts');
       const totalPrice = appetizer.price + main.price + dessert.price
       return `This meal includes ${appetizer.dish} for an appetizer, ${main.dish} for the main dish, and ${dessert.dish} as the dessert. The total price will be ${totalPrice}`
   }

};

//appetizers added to menu
menu.addDishToCourse('appetizers', 'Mozzarella Sticks', 8);
menu.addDishToCourse('appetizers', 'Chili Cheese Fries', 7);
menu.addDishToCourse('appetizers', 'Spinach-Artichoke Dip', 9);

//mains added to menu
menu.addDishToCourse('mains', 'Bison Burger', 12);
menu.addDishToCourse('mains', 'Cheese Ravioli', 11);
menu.addDishToCourse('mains', 'Club Sandwich', 10);

//desserts added to menu
menu.addDishToCourse('desserts', 'Chocolate Brownie', 4);
menu.addDishToCourse('desserts', 'Créme Brûlée', 6);
menu.addDishToCourse('desserts', 'Ice Cream Sundae', 5);

let meal = menu.generateRandomMeal();

console.log(menu.courses)

console.log(meal);

