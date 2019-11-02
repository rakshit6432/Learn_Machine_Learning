<h1>Week 1: Agile Fundamentals</h1>



<h2>Introduction</h2>


<h3>What software development looks like?</h3>

Software Development Process in Waterfall Model:
1. Requirements: what exactly you need to build.
2. Design: what are the different components that we need to build and how they're going to work together.
3. Implementation: start coding and do unit tests, integration tests or card verification and functional testing
4. Verification: Do a User Acceptance Testing.
5. Operations and Maintenance: software in production, bug fixes, new features based on consumer requests.

Problems with such a model:
- very difficult to predict the requirements one year or two a year ahead.
- misinterpretation of requirements might go undetected till verification.
- integration issues between the different components.

As a solution different variants of the waterfall model evolved:
- V Model which focuses a lot on testing.
- Sashimi Model or RUP Model that focuses a lot on overlapping different phases.
- Incremental model where you do the requirements in one shot but then you do the design, testing, and deployment in increments.
- Spiral Model which is a very risk driven approach.

The cons of the waterfall method also led to the evolution of the __Agile__ mindset and models like Scrum and Kanban and XP that helped implement this mindset. The basic idea behind all of this model was that instead of building this whole one year cycle, you build in short cycles adopting to the changes of the market and the user needs.

Due to this, the idea of _continuous integration_ and _automated testing and deployment_ was born.

<h3>Intro to Software Development Models</h3>

Classification of different models falls into two main categories:

- _Predictive_ vs _Adaptive_:
    - predictive: good understanding of the requirements so you build the product in one shot.
    - adaptive: general understanding of the requirements so you start with Proof of Concepts and small versions and use user feedback to iterate and implement the next version of the product.

- _Incremental_ vs _Iterative_:
    - incremental: good idea of the requirements but you build the product in increments, you break the product into smaller pieces.
    - iterative: general understanding of the requirements so you build the product iteratively and you replace your previous iteration with the newer ones with enhancements.


<h2>Agile Values and Principles</h2>


<h3>Why Agile?</h3>

The problem with the waterfall model was not that requirement translation issues were found, or the requirements were incorrect, it was the time we were finding these issues. Due to the cost of change, the later we find the problem, the more costly it's going to be. So the foundation of the Agile mindset was to try to reduce the learning cycle and to keep the cost of change down. Agile principles made the industry realize that software development is a creative process, and we need adaptive methods to be successful at it.

<h3>Agile Manifesto: Values</h3>

1. __Individuals and Interactions__ over Processes and Tools.

2. __Working Software__ over Comprehensive Documentation.

3. __Customer Collaboration__ over Contract Negotiation.

4. __Responding to Change__ over Following a plan.

<h3>Agile Manifesto: Principles</h3>

1. Our highest priority is to _satisfy the customer_ through early and continuous delivery of valuable software.

2. _Welcome changing requirements_, even late in development. Agile processes harness change for the customer’s competitive advantage.

3. _Deliver working software frequently_, from a couple of weeks to a couple of months, with a preference to the shorter timescale.

4. Business people and developers must _work together daily_ throughout the project.

5. Build _projects around motivated individuals_. Give them the environment and support they need, and trust them to get the job done.

6. The most efficient and effective method of conveying information to and within a development team is _face-to-face conversation_.

7. _Working software_ is the primary measure of progress.

8. Agile processes promote _sustainable development_. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.

9. Continuous _attention to technical excellence and good design_ enhances agility.

10. _Simplicity_–the art of maximizing the amount of work not done–is essential.

11. The best architectures, requirements, and designs emerge from _self-organizing teams_.

12. At regular intervals, the _team reflects_ on how to become more effective, then tunes and adjusts its behavior accordingly.


<h2>Applying Agile Mindset</h2>


<h3>Benefits and Challenges of Agile</h3>

<img src="../2. Agile Software Development/images/agile_pros.png">

<img src="../2. Agile Software Development/images/agile_cons.png">

<h3>Agile: When to Use and When NOT to!</h3>

- Can be useful for small, medium and large scale projects.
- Can be useful for mission critical projects like government projects.
- Not suitable for predictive and repeatable work.
- Pre-requisites should be met:
    - Customer collaboration
    - The team should be set up for change by following engineering principles.

<h3>Applying an Agile Mindset to a Project</h3>

<img src="../2. Agile Software Development/images/agile_mindset_1.png">

<img src="../2. Agile Software Development/images/agile_mindset_2.png">

<img src="../2. Agile Software Development/images/agile_mindset_3.png">

<img src="../2. Agile Software Development/images/agile_journey.png">

<h3>Agile Frameworks</h3>

- Scrum: based on one to four week cycle, where you take part of your project and you define, develop,  design and test your software. Your product is developed incrementally.

- Kanban: based on a continuous flow model where you basically try to optimize your existing software development process.

- Scrumban: Combination of Scrum and Kanban.

- XP: has most of the practices of the Scrum but it also defines some additional engineering practices.

- Lean Startup: helps you if you have a lot of unpredictable market or industry.



<h1>Week 2: Requirements and Planning</h1>



<h2>User Stories and Requirements Gathering</h2>


<h3>Gathering Requirements: The agile way</h3>

The 3C's of user story process:

<img src="../2. Agile Software Development/images/story_process.png">

Second part of this agile approach is called the _Adaptive_ where the agile approach accepts that we don't know the needs upfront and we are going to discover the needs, so we allow the requirements to change over time.

<img src="../2. Agile Software Development/images/agile_approach.png">

<h3>User Stories: The currency of agile development</h3>

The main component of user stories are the 3C's of the user stories:
- Card - Token for conversation
- Conversation to build Shared understanding
    - __Who__ (wants) __What__ (and) __Why__
    - Record fact/info to help you recall the conversation
    - Discuss what happens outside the software
    - Discuss what can go wrong

- Confirmation - __Acceptance Tests__

<img src="../2. Agile Software Development/images/user_story_template.png">

__How to write acceptance tests:__

<img src="../2. Agile Software Development/images/acceptance_tests.png">

Another idea in agile approach is something called __Spike_ and these stories are needed when you have to do some kind of an _exploratory work_ or let's say, you have to choose a tool or technology or a software to build your to build what you're building so these are mostly used as _Knowledge gathering stories_, which are _Time boxed_ and will have a _clear definition of done_.

<h3>Characteristics of good user stories</h3>

<img src="../2. Agile Software Development/images/characteristics_ of_user_stories.png">

<h3>Generating User Stories</h3>

1. __User Story Writing Workshop__

    _Goal:_
    - Write as many stories as you can for the selected theme.

    _Who to invite?_
    - Product owner and other stakeholders who knows user needs
    - Scrum master
    - Development team

    _How long?_
    - Few hours to few days

    _User story writing workshop agenda_

    <img src="../2. Agile Software Development/images/user_story_agenda.png">

    _Characteristics of good product backlog_
    - Detailed Appropriately
    - Emergent
    - Estimated
    - Prioritized

2. __Story Mapping__

    _Technique to_
    - Discover user needs
    - Organize and prioritize story backlog
    - Understand and communicate user needs
    - Plan releases and development

    _Story map structure_

    <img src="../2. Agile Software Development/images/story_map_structure.png">

    _Steps of creating a story map_

    <img src="../2. Agile Software Development/images/story_map_step_1.png">

    <img src="../2. Agile Software Development/images/story_map_step_2.png">

    <img src="../2. Agile Software Development/images/story_map_step_3.png">

    <img src="../2. Agile Software Development/images/story_map_step_3b.png">

    <img src="../2. Agile Software Development/images/story_map_step_4.png">

    _Why create them?_
    - Discover user needs - especially help discover missing pieces
    - Understand and communicate user needs:
        - Help communicate at multiple levels
        - Help tell a story
    - Planning:
        - Provide a useful context for prioritization
        - Plan releases in complete and valuable slices of functionality
        - Organize and prioritize story backlog
    - Foster co-ownership
    - Flexible


<h2>Agile Estimation and Planning</h2>


<h3>Agile Estimation and Planning</h3>

<img src="../2. Agile Software Development/images/agile_planning.png">

__Release Planning:__

<img src="../2. Agile Software Development/images/release_planning.png">

__Agile Approach for Estimation:__

- _Effort vs Duration_

<img src="../2. Agile Software Development/images/Effort_vs_Duration.png">

- _Accuracy vs Precision_

<img src="../2. Agile Software Development/images/Accuracy_vs_Precision.png">

- _Relative vs Absolute_

<img src="../2. Agile Software Development/images/Relative_vs_Absolute_sizing.png">

<img src="../2. Agile Software Development/images/Relative_vs_Absolute.png">

<h3>Estimation Styles and Process</h3>

__Estimation Process__

- Who Estimates?
    - Development Team

- How long does it take?
    - Depends on style, method, number of stories, understanding, knowledge, expertise, no.of team members

- Estimation Styles
    - Simple - Free form
    - Planning poker
    - Card Sorting

__Planning Poker__

1. Everybody gets the estimation
2. Explain the story
3. Understand the story
4. Estimate and put one card down
5. Open cards
6. If consensus, move to next item
7. Else discuss variations and go back to step 3

_Pros and Cons_

- Time consuming
- Uncover misunderstanding
- Collective ownership
- Engaged
- Good for backlog grooming session.

__Card Sorting__

<img src="../2. Agile Software Development/images/Card_Sorting.png">

<h3>Velocity</h3>

Velocity is amount of work that a team is getting in a sprint. To calculate the velocity of a sprint you just finished, you take all the stories you finished and you add together. Velocity is also used for selecting stories for an upcoming sprint. There are several ways you can do this, the simplest is, you can use the velocity of the _last sprint_, or you can take the _average_ of the last x number of sprints, or you can take the _velocity range_ of last x sprints.

<h3>Release Planning</h3>

There are two types of release planning:

1. __Fixed Scope__

    - Fixed scope, variable date
    - When will you deliver Release?
        1. Decide sprint length
        2. Calculate velocity (or velocity range)
        3. Total up estimate for selected stories
        4. Total Estimate / Velocity ~= # sprints
        5. number of sprints times sprint length = duration

    <img src="../2. Agile Software Development/images/Fixed_scope.png">

    _How to Select Stories?_

    <img src="../2. Agile Software Development/images/select_stories.png">

2. __Fixed Date/Time__

    - Date fixed so scope changes
    - What are you going to deliver?
        1. Groom backlog (if not done so)
        2. Calculate velocity range
        3. Select sprint length
        4. Calculate # sprints
        5. Calculate release capacity = #sprint * velocity (use two times to get range)
        6. Include items from backlog (starting at top) until total point exceed points range: will have, might have

        <img src="../2. Agile Software Development/images/Fixed_date.png">

<h3>Release Tracking</h3>

There are three methods that we can use to get a sense of are we on track or not:

1. Release Burn up

<img src="../2. Agile Software Development/images/release_burn_up.png">

2. Story Board

<img src="../2. Agile Software Development/images/story_board.png">

3. Cumulative Flow

<img src="../2. Agile Software Development/images/cumulative_flow.png">



<h1>Week 3: Scrum</h1>





<h1>Week 4: XP</h1>
