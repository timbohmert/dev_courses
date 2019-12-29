//recorded hours of sleep during one week
const getSleepHours = day => {
    switch (day) {
        case "Sunday":
        case "Wednesday":
        case "Thursday":
        case "Saturday":
            return 8
            break;
        case "Monday":
        case "Friday":
            return 6
            break;
        case "Tuesday":
            return 7
            break;
        default:
            break;
    }
}

//calculate actual hours slept for the week
const getActualSleepHours = () => {
    return getSleepHours("Sunday") + getSleepHours("Monday") + getSleepHours("Tuesday") + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday');
}


//calculate my ideal hours of sleep per week
const getIdealSleepHours = hours => hours * 7

//calculate sleep debt with actual versus ideal
const calculateSleepDebt = () => {
    actualSleepHours = getActualSleepHours();
    idealSleepHours = getIdealSleepHours();
    if (actualSleepHours == idealSleepHours) {
        console.log("You gaught a Goldilock's amount of sleep - just right!");
    } else if (actualSleepHours > idealSleepHours) {
        console.log(`Great job sleeping with your extra ${actualSleepHours - idealSleepHours} hours over ideal, but how about doing better job with wokeness.`);
    } else if (actualSleepHours < idealSleepHours) {
        console.log(`Hey there grouch, you slept ${actualSleepHours - idealSleepHours} less than ideal. Why don't you try getting more sleep?`);
    } else {return 'Error'}
}