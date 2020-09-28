/*
WorkAround is a human resources program that returns basic information about an employee, based on Employee.salary data. Using WorkAround, one can use an employee’s Employee.salary data to:

-return the cadre of the of the employee, in other words, whether this employee is entry level, mid level, or senior level.
-calculate employee tax rates
-return employee benefits
-calculate employee bonuses
-calculate the total amount an employee can be reimbursed based on the total value of their health, housing, or wellness benefits

WorkAround currently contains the data and functions in a single file, though they would like to modify the program so it makes use of JavaScript modules. Specifically, WorkAround asks you to demonstrate the different ways to export and import modules.
*/

//base code provided by codecademy. Tim Bohmert wrote code to create modules


let Employee = {
    salary: 100000
}

let payGrades = {
  entryLevel: { taxMultiplier: .05, benefits: ['health'], minSalary: 10000, maxSalary: 49999 },
  midLevel: { taxMultiplier: .1, benefits: ['health', 'housing'], minSalary: 50000, maxSalary: 99999 },
  seniorLevel: { taxMultiplier: .2, benefits: ['health', 'housing', 'wellness', 'gym'], minSalary: 100000, maxSalary: 200000 }
};

export const getCadre = () => {
if (Employee.salary >= payGrades.entryLevel.minSalary && Employee.salary <= payGrades.entryLevel.maxSalary) {
    return 'entryLevel';
  } else if (Employee.salary >= payGrades.midLevel.minSalary && Employee.salary <= payGrades.midLevel.maxSalary) {
    return 'midLevel';
  } else return 'seniorLevel';
}

export const calculateTax = () =>{
return payGrades[getCadre()].taxMultiplier * Employee.salary;
}

export const getBenefits = () => {
return payGrades[getCadre()].benefits.join(', ');
}

export const calculateBonus = () => {
return .02 * Employee.salary;
}

export const reimbursementEligibility = () => {
  let reimbursementCosts = { health: 5000, housing: 8000, wellness: 6000, gym: 12000 };
  let totalBenefitsValue = 0; 
  let employeeBenefits = payGrades[getCadre()].benefits;
  for (let i = 0; i < employeeBenefits.length; i++) {
    totalBenefitsValue += reimbursementCosts[employeeBenefits[i]];
  }
  return totalBenefitsValue;
}

export default Employee;