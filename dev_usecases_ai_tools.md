
#### Share this post

[![](https://substackcdn.com/image/fetch/w_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00eb629f-dff1-4050-ac97-f3d2bd35388e_2000x1400.png)![Engineering Enablement](https://substackcdn.com/image/fetch/w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44d786b5-325a-45ed-b716-583f40f53415_444x444.png)Engineering EnablementHow developers want to use AI tools](https://substack.com/home/post/p-147225142?utm_campaign=post&utm_medium=web)Copy linkFacebookEmailNotesMore

How developers want to use AI tools
===================================

### A Microsoft study on the use cases for tools like Copilot, and developers' main concerns with using AI tools.

[![](https://substackcdn.com/image/fetch/w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52563aeb-f45b-4398-bd96-947897fc3d59_1806x1865.png)](https://substack.com/@abinoda)[Abi Noda](https://substack.com/@abinoda)Aug 09, 202410
#### Share this post

[![](https://substackcdn.com/image/fetch/w_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00eb629f-dff1-4050-ac97-f3d2bd35388e_2000x1400.png)![Engineering Enablement](https://substackcdn.com/image/fetch/w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44d786b5-325a-45ed-b716-583f40f53415_444x444.png)Engineering EnablementHow developers want to use AI tools](https://substack.com/home/post/p-147225142?utm_campaign=post&utm_medium=web)Copy linkFacebookEmailNotesMore[1](https://newsletter.getdx.com/p/developer-use-case-with-ai-tools/comments)[Share](javascript:void(0))

*This is the latest issue of my newsletter. Each week I cover the latest research and perspectives on developer productivity.*

Subscribe

---

This week I read [Towards Effective AI Support for Developers: A Survey of Desires and Concerns](https://www.microsoft.com/en-us/research/publication/towards-effective-ai-support-for-developers-a-survey-of-desires-and-concerns/) from Microsoft. In this paper, researchers sought to understand how developers view AI, how they want to use it, and what their top concerns are in adopting it. 

Google recently released a [similar paper](https://newsletter.getdx.com/p/developers-want-from-generative-ai?utm_source=publication-search) where they looked into how developers want to work with AI. While Google's findings were more general (“developers want AI tools to support simpler tasks and reduce toil”), Microsoft's paper is more specific. Also, Google's paper talks about how they decide where to use AI tools within the company—Microsoft's paper doesn't cover their approach to this.

My summary of the paper
-----------------------

This paper shares the results from a study with nearly 800 developers at Microsoft. The survey excluded any developers directly working on AI-based tools.

### What developers are most interested in using AI for

The survey included the question, “Which of the following aspects of your job would you most like to see AI tools help with?” Developers could select up to 3 items from the provided list of 17 response options.

Most developers (96%) want AI to help with routine tasks such as generating tests or writing documentation. 37% of developers want AI to simplify administrative overhead tasks, such as email parsing and task management.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29163ffc-c957-46e4-b3e7-82b8cf0d70a1_1516x1284.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29163ffc-c957-46e4-b3e7-82b8cf0d70a1_1516x1284.png)



The top use case that Microsoft developers want AI tools for is to generate unit, integration, and functional tests. This makes sense: testing is valuable, but it’s not always the most exciting part of the job. Using AI for this task would, in theory, not just alleviate some of the monotony but could also result in higher-quality tests.

The other most common task developers want AI for is to analyze code for defects, vulnerabilities, and optimizations. This kind of work can be repetitive, and having AI check code might give developers more confidence in their results.

Writing documentation was also a common use case developers want help with. While developers emphasized that AI-generated documentation shouldn’t be blindly trusted—it's important to review and edit for accuracy—these tools can take care of some of the more tedious aspects of the task.

Each of the top four tasks that developers are interested in using AI for are focused on helping them with work that is necessary but repetitive or undifferentiated. This fits with what [Google’s study](https://newsletter.getdx.com/p/developers-want-from-generative-ai?utm_source=publication-search) found—that developers want AI to reduce toil but not take away from the most rewarding parts of their job. That might explain why “writing new code or refactoring existing code” was slightly lower on the list, with 25% of respondents choosing it as a desired use case. Those who did choose "writing new code and/or refactoring existing code" as a desired use case wanted AI tools to help reduce the time spent on boilerplate code.

The researchers note that tenure didn’t make that much of a difference in which items were selected. The only exceptions were “evaluating performance to help identify areas of growth” and "clarifying requirements,” which were both more commonly chosen by developers with fewer years of experience versus more senior developers.

### Apprehensions developers have with using AI tools

To understand why developers might not adopt AI tools, the researchers included this question in their survey: “What worries you the most about integrating AI into your daily workflows?” They provided a list of options that developers could choose from.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2958f79-5bce-43ff-9079-903cf55dc2fd_1522x1684.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2958f79-5bce-43ff-9079-903cf55dc2fd_1522x1684.png)



The biggest concern developers have with AI tools is that they can be more gimmicky than helpful. This matches what we found in our [State of DevEx report](https://newsletter.getdx.com/p/state-of-developer-experience-2024): leaders might be overly optimistic about AI tools, while developers aren’t as impressed. It's important for AI tools to be technologically advanced, but it's equally crucial for those introducing them to be transparent about what these tools can really do.

Many developers also worry that AI could deteriorate the quality of their work. As one study participant said, “I am worried that AI will create answers that give the appearance of correctness, but are not actually correct.” This underscores the need for transparency from AI tools and also highlights the importance of human oversight.

[Another study](https://newsletter.getdx.com/p/barriers-to-ai-adoption-engineering) exploring the barriers to AI adoption similarly found that “limited capabilities relative to expectations” was a top reason why these tools don’t get the expected levels of adoption. That study also found that a fear of decreased skills, potential judgement from peers, and not having a culture of sharing inhibited AI adoption. 

### **Author recommendations**

This survey surfaced a few themes related to the need for transparency, education, and humans being in the loop. The authors leave with a few specific recommendations to improve AI tool adoption:

* Help teams understand how AI models work and how AI tools can be applied to existing technologies. Equip leaders with the skills needed to guide their teams through these changes. Bootcamps, online courses, and workshops are great formats for this.
* Be clear about which AI tools are being used and what they’re meant to do.
* Instead of relying entirely on AI, find a balance where humans stay involved, especially for critical tasks.

Final thoughts
--------------

This paper advances the conversation about how organizations can get the most out of their investments in tools like Copilot. One common challenge is figuring out the best ways to use these tools—this paper provides helpful insights on what those use cases might be. It also explores other reasons why an organization might not see the adoption they were expecting.