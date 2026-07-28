// Functions

function sayHello() {
    console.log("Hello, DevOps Engineer!");
}

// Function with Parameters
function deployToRegion(region) {
    console.log("Deploying to region: " + region);
}

function configureService(serviceName, tier) {
    console.log("Configuring " + serviceName + " with " + tier + " tier.");
}


// Calling function
sayHello();

// Calling function with Parameters
deployToRegion("us-east-1");
configureService("EC2", "t2.micro");