---
layout: post
title: "Insight into 20/20 and visual acuity"
tldr: "a brief intro of what visual acuity, diopter and some interesting data"
tags: [data science, bio, sight, visual, acuity, diopter]
---

[1]: http://www.iovs.org/content/45/10/3458/F1.expansion.html
[1a]: http://en.wikipedia.org/wiki/Visual_acuity#Normal_vision
[1b]: http://en.wikipedia.org/wiki/Visual_acuity#Expression
[1c]: http://www.eye-sim.com/converter.html
[1d]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1616205/
[1e]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1616205/pdf/healthservrep00026-0041.pdf
[1f]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2031704/
[1g]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2031704/pdf/pubhealthreporig01071-0027.pdf
[1h]: http://www.vdwoxford.org/resources/AO_Poster_Nov2008-v3_final.pdf
[1j]: http://en.wikipedia.org/wiki/File:Refractive_errors_world_map_-_DALY_-_WHO2004.svg
[1k]: http://archopht.jamanetwork.com/article.aspx?articleid=424548

The abilities for each sensory organ follows a different distribution. My guess is that the distribution for the visual abilities among our species must have fairly low variance. I would assume that by natural selection, the genes related to better visual abilities would have been more likely passed along, since humans are such highly visual creatures. (It would be difficult for our ancestors to engage in persistent hunting if they couldn't see their prety after some amount of distance.)

The high reliance of humans on our vision also explans the often unquestioned amazing demand for corrective lenses, and such a strong cultural urge to make them fashionable items.

Conversely, the use of hearing aids is much less prevalent and less commonly accepted. If our hearing mattered as much as our seeing, we would see a lot more people willing to wear hearing aids even if they had minor hearing loss.

Before I looked at any data, I was trying to speculate what the distribution looked like. I wasn't sure whether the distribution for visual acuity would be one-tailed or two-tailed. The two-tailed distribution like the normal distribution would employ that there are equal amounts of people who have better or worse vision than the average. As I quote from the article on Wikipedia about [visual acuity][1a]

> In humans, the maximum acuity of a healthy, emmetropic eye (and even ametropic eyes with correctors) is approximately 20/16 to 20/12

It seems empirically that there are many more people who need glasses than those who have above average vision. Also, we can see the table on the right hand side of this [article ][1b] that there are many more values worse than 20/20 rather than better. Although we have no data, it would appear to me that a one-tailed distribution would be more appropriate since our distribution is unlikely to be symmetric.  

Before we move on, apparently, there isn't a straightforward conversion from diopter (which is what your glasses prescription is) to your visual aculity (which is what your eyes are capable of seeing). Your visual aculity is a measure of what your eyes are capable of, while your diopter is supposed to be the set of prescription to allow you to achieve the closet to perfect vision. Especially, if you have myopia *AND* farsightedness, then your eyeglass prescription will generally have a different set of considerations. But in general, if you trust the internet, [here][1c] is a conversion site you can use. (Search Diopter to 20 20 for more sites)

Apparently, with DV spherical -3.00 for both eyes, my vision is roughly estimated to be about 20/150 to 20/200, meaning I can see at 20 feet what other people can see at 150 to 200ft. Apparently, there's actually some amount of data on this very topic but was initially difficult to find because it was named incorrectly. But I found this interesting graphic on this [poster][1h] on the distribution of unaided visual acuity. 

<img src="/assets/images/dist_visual_acuity.png">

As you can see that the distribution actually looks pretty normal to me. 

There is apparently also this whole issue of presbyopia. Normal healthy eyes can focus on a huge range of distances. But when you age, your eyes lose that ability usually affecting your ability to see really close things. Meaning that if you already myopia, you can't seen near as well as far. I'm not sure how that factered into their study which seemed to be primarly on the young, but I'm unsure. 

Finally, a [graphic][1j] to show that even among different countries in the world, the distribution of visual acuity is different. And another [paper][1k] that it changes over time as well

sources

1. http://en.wikipedia.org/wiki/Eyeglass_prescription
2. http://en.wikipedia.org/wiki/Visual_acuity
3. http://en.wikipedia.org/wiki/Dioptre
4. [Distribution of Visual acuity in Egypt][1d]
5. [Visual acuity and field of vision of urban and rural Egyptians][1f]

Footnotes

1. Apparently though, there is [this][1d] study done in the 1970s in Egypt on the visual acuity where the eyesight of about 150,000 people was measured. They separate the results into age group and they have seven levels for visual ability 6/6, 6/9, 6/12, 6/15, 6/20, 6/30, 6/60 or less. A note from the methodology of the data collection from a [paper][1g] by the same authors shows that 

>The person was examined with his eyeglasses on if he had any. The best visual acuity of each eye was determined by starting with a visual acuity of 6/60 (20/200) and by successive steps to determine the best visual acuity. If the better eye had a visual acuity of 6/60 or less, correcting lenses were added after retinoscopy to improve the visual acuity to at least 6/30. If the person's visual acuity was 6/60 or less in the better eye with best correction, he was referred to the ophthalmologist as blind 

This to me raises several problems. If the data collection is done with corrective senses, then ideally everyone should actually have 20/20 vision. And with eyeglass manufacturing technology improving, I'm assuming that the best correction lense of the 1970s is different from what it is today. Thus, the data collected in this paper doesn't say very much about the distribution of visual acuity in a general population, but just a dataset also confined to the general eyeglass wearing rate among the sample and also the best corrective lense that was available during the exmaination.

