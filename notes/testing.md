Testing
======

# Types of Testing

1. Manual human testing
    * As useful as anecdotal evidence
1. Unit: Each function/class/method is tested
    * Write piece of code with a known end state, check that end state is achieved
    * Majority of code coverage comes from unit tests
1. Integration: Test if components work together as expected
1. Functional: Does the service/subsystem/system work as expected
1. E2E (End 2 End): Does the system work in context
1. Regression: Do old tests pass for new builds
1. Smoke: Quick test of major functionality
    * One of the least understood
    * Major features of a software product version
        * Can user login and logout
    * Major blocking tests: these must work in order to release version of a project
1. Acceptance: Pre-release (alpha & beta builds of program)
    * Implementing acceptance critrea of customer/sponsor
    * Base requirements test suite must pass in order to create deployment
    * This style of testing is generally done to create candidate builds for an application
        * Goal is to find where application
        * Sandbox build: Non-production environment, non-complete implementation of the product that is generally used for futher testing
            * Generally used internally within teams for testing
        * Alpha build: Non-production environment, full implementation of the project for further internal testing
            * Generally scale is not considered and users are not expected to use this build
        * Beta: Semi-production environment, full implementation of the product intended to gather feedback or market the product to future users
            * Goal is to be as close to production as possible
            * Often is invite only, or limited to the general public
            * Now it is becoming common practice to do 2 betas (open, closed) in favor of traditional Alpha -> Beta -> Prod deployment flow
        * Production: Production release version of the product
1. System: Do app work when system context changes (OS/Browser/etc)
    * Systems tests are referred to in matrixes of operating systems in combination with different web browsers
        * Goal is to ensure that no combination of softwares/platforms/browser escapes testing
1. Stress testing: Does the application work under extreme load
    * How does the site handle unusual scenarios
        * What if the system it loads on has low memory and low ram
1. Performance: How does the system work under extreme load
    * How does that site handle larger amounts of requests for data
1. Usabilty: How usable is the system to users
    * Make people use your product
        * Important to not tell users how to work the application; goal is to make application seamless and easy to pick up and understand
    * Collecting feedback starts in sandbox environment and continues as the environments are scaled up
1. Negative: Test that known negative cases fail properly
    * Handle unexpected events
    * Check unexpected user input fails properly

# Writing Test Plans

## Creation steps

### Product analysis

You need understanding of

* What does product do
* Who is product for
* Who uses it
* What are the requirements

Approach

* Interview everyone involved in project
* Review documentation of the plan

System Walkthrough

* Go through the system in detail to develop initial issues, risks, thoughts

Think through negative cases

* What unexpected and unusual behavior can users exhibit using the application

### Test strategy - scope

* Scope
  * Prioritization
    * Components that will be tested in scope
    * Components that might be tested
    * Components that will not be tested
  * Budget and Schedule
    * Detailed or rough
  * Skills and talent
* Testing types
  * Which testing types will be focus of the project and which will be ignored
* Risks and issues
  * Document risks of the project
    * Lack of experience
    * Lack of skills
    * Lack of resources
* Logistics
  * Who will test
  * When will testing occur

### Test objectives

1. Find as many defects (bugs) as possible
1. List all features which may need to be tested
1. Define the target or goal of the test based on the features

**Example**: Banking

1. Users and accounts
    * Login and logout
    * Create new and edit
1. Functionality
    * Deposit, withdrawl, balance, account, etc.
1. Security
    * AuthN, AuthZ, protections
1. Performance
1. Usability

### Test criteria

Suspension: What will make our team suspend testing until things are fixed

* Ex: If >= 10% of test cases fail then suspend and fix test cases

Exit criteria: When can we stop testing

* Targeted result of tests
  * Ex: If >= 95% of all critical test cases must pass

Run rate

* \# of test cases executed / total # of test cases

Pass rate

* \# of tests passing / total # of test cases

### Resource planning

Humans

* Management: Define project and aquire resources
* Testers: Those respon
* SDET: Implement test cases
* Admin: Manage test environments and frameworks 

### Test environment

* Hardware and software on which testing occurs
* Sandboxes and alpha testing
* Performance and stress frameworks