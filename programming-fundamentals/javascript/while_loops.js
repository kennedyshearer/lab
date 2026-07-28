// While Loops

let instantCount = 0;
const targetCount = 5;

while (instantCount < targetCount) {
    console.log("Launching EC2 instance #" + (instantCount + 1));
    instantCount++;
}