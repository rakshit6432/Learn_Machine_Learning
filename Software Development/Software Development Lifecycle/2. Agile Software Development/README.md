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



<h2>Scrum Overview</h2>


Scrum works on this one to four week sprint where you take part of your product, and you define your design, your build, and your test. And then you get product feedback from the stakeholders and then repeat the cycle again and again.

There are three roles that are defined in Scrum:

- __Product Owner__:
    - Define what needs to be done and in what order.

- __Scrum Master__:
    - Help the team stay true to the Scrum values and principles.
    - Facilitate most of the meetings in the team.
    - Drive resolution for some of the roadblocks.

- __The Team__:
    - Self organizing and they do the building of the software

__Steps in a Scrum Framework:__

1. Product owner gets input from customers, users and stakeholders and creates a _Product Backlog_ with user prioritized stories.

2. The team gets together for a _Sprint Planning Meeting_ and pick the top stories to work on.

    a. The product owner reviews those stories with the team and answer any questions

3. The team gets together again and tasks the user stories - _Sprint Backlog_

4. The team commits to the stories.

5. Start Sprint

    a. Get together for daily standup

6. Finish Sprint

    a. _Sprint Review_: reviews the work done with the stake holders and clients.

    b. _Sprint Retrospectives_: talk about how we can optimize the process.

To keep track of the sprint and the goals the team uses a _burn down_ or a _burn up_ chart

<img src="../2. Agile Software Development/images/scrum_framework.png">


<h2>Sprint Planning and Tracking</h2>


<h3>Sprint Planning</h3>

Before you do the sprint planning, you need to do some prep work called __Backlog Grooming__:

- Removing user stories that no longer appear relevant.
- Creating new user stories in response to newly discovered needs.
- Re-assessing the relative priority of stories.
- Assigning estimates to stories which have yet to receive one.
- Correcting estimates in light of newly discovered information.
- Splitting user stories which are high priority but too coarse grained to fit in an upcoming sprint.

Once the Backlog is upto date, the next process is __selecting and preparing stories__:

- Use the story map
- Use your prioritized backlog and just start from the top picking stories based on your velocity

Once the story is selected make sure the stories are ready to be worked upon (who, what, why, acceptance test, any major dependencies).

Once the preparation is done, you can start __sprint planning__. There are two ways you can do this:

- One step: Select one story at a time, task it out until capacity is reached

- Two step:
    - Select stories based on velocity
    - Task out and gain confidence

__Steps for sprint planning__

1. Determine sprint capacity:

    <img src="../2. Agile Software Development/images/determine_capacity.png">

2. Review and Define Sprint goal (if any)

3. Review potential stories

4. Acquire confidence: design discussion and task out stories

5. Refine sprint goals if required.

6. Make commitment

7. Put the stories and tasks on the task wall.

<h3>Sprint Tracking</h3>

There are three methods of Sprint Tracking:

- __Burn down__: work left

    <img src="../2. Agile Software Development/images/burn_down.png">

- __Burn Up__: work done + total work

    <img src="../2. Agile Software Development/images/burn_up.png">

- __Task board__:

    <img src="../2. Agile Software Development/images/task_board.png">


<h2>Sprint Review, Retrospective and Sprint Execution</h2>


<h3>Sprint Execution and Daily Standups</h3>

__Sprint Execution__

- Let the developers pick the stories rather than assigning them
- Limit the work in progress
- Parallel work vs Swarming
- Generalists vs Specialists
- Discipline: Make sure to follow what the team decides to do
- Following Engineering practices

__Daily Standup__

- What?
    - Common: Three questions- What did I do yesterday? What I'm going to do today? And are there any road blocks?
    - Alternatives: Devs talk about stories from priority order (story focused standup)

- Who?
    - Core Team + any stakeholder who wants to attend

- Purpose?
    - Daily team planning
    - COllaborate
    - Identify blockers
    - This isn't really a status check meeting

- Tips
    - Show the story board
    - Keep it short

<h3>Sprint Review</h3>

- Purpose:
    - Review work done and learning from the sprint
    - Get feedback and adjust future direction
    - Celebrate

- Who?
    - Core team
    - Stakeholder
    - Anybody and Everybody

- How long?
    - 1-2 hrs

- What happens?
    - Summarize everything that happened, your planning, what you did and roadblocks
    - Demo the work
    - Discuss the sprint with stakeholders and get feedback
    - Adapt a future direction of your product if needed

<h3>Sprint Retrospective</h3>

- Who?
    - Core Team

- When?
    - At the end of each sprint iteration

- Purpose?
    - Continuous Improvement

- What happens?
    - What's working?
    - What's not working?
    - Action Items?

You can also do an alternative focused retro for any stories that's not finishing:

- Steps:
    - Set the atmosphere
    - Share context
    - Identify Insights
    - Determine Actions
    - Close the retrospective

- Follow through



<h1>Week 4: XP</h1>



<h2>XP</h2>


<h3>XP Overview</h3>

XP stands for eXtreme Programming. extreme because it takes the good practices to extreme. For example if code review is good, why not pair developers together from the beginning and let them provide constant feedback rather than just doing code reviews at the end.

In concrete terms, XP defines a set of values, principles, and practices. Now, since it took everything to an extreme, it ran into some controversies. One XP is prescriptive compared to many of the other lightweight agile practices, like Scrum, two pair programming, and a lot of industries say that this is too much, similarly about incremental design, three scalability of XP method, it cannot scale to bigger teams and it's okay for small to medium-sized company.

<h3>XP Values</h3>

Five values behind the XP practices and methods:

- Simplicity: Maximizing value by doing only what is necessary.
- Communication: Face to face daily and work together on everything from requirement to code.
- Courage: Tell truth about progress, adapt to change and don't document failure because we will change.
- Feedback: Generate as much feedback as a team can handle to iterate and improve.
- Respect: each other.

<h3>XP Practices</h3>

- Do practices while keeping their purpose in mind.
- Keep making progress towards ideal state in mind.
- Experiment
- Practices work well together.
- Primary and Corollary practices.

__Primary Practices:__

- Sit together: open and highly collaborative working environment.
- Whole team: Team composition is Dynamic and you have everyone you need for a project and no fractional people.
- Informative workspace: Dynamic information and set up workspace so it can help anyone get an idea on the project
- Energized work: working hours, incremental improvement and rest.
- Pair programming.

__Corollary Practices:__

- Stories: Are flexible, estimated early, unit of functionality where development resolves and keep them visible.
- Weekly Cycle: plan weekly, review progress, select week's worth work and break stories into tasks. Gradually reduce planning time.
- Quarterly cycle: plan work quarter at a time, focus on the big picture, plan the themes for the quarter.
- Slack: build some slack time into the process by adding some low priority tasks that can be skipped or 20% personal time and avoid aggressive commitments.
- Ten minute build: build and run all the test within  10 minutes.
- Continuous integration: synchronous and asynchronous integration
- Test first programming.
- Incremental design: invest little time in design everyday, refactor and architecture emerges over time.

<h3>XP Process Model</h3>

<img src="../2. Agile Software Development/images/xp_process.png">

<h3>Scrum vs XP</h3>

__Differences Between Scrum and Extreme Programming__

There are four main differences between Scrum and XP:

1. Scrum teams typically work in iterations (called sprints) that are from two weeks to one month long. XP teams typically work in iterations that are one or two weeks long.

2. Scrum teams do not allow changes into their sprints. XP teams are much more amenable to change within their iterations. As long as the team hasn’t started work on a particular feature, a new feature of equivalent size can be swapped into the XP team’s iteration in exchange for the unstarted feature.

3. Extreme Programming teams work in a strict priority order.  By contrast, the Scrum product owner prioritizes the product backlog but the team determines the sequence in which they will develop the backlog items.

4. Scrum doesn’t prescribe any engineering practices; XP does. For example engineering practices like test-driven development, automated testing, pair programming, simple design, refactoring and so on.
