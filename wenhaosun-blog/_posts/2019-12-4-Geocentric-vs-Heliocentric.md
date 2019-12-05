---
layout: post
title: Could a machine learn the structure of the solar system?
image: /assets/img/blog/Geo_vs_Helio.PNG
description: >
  Given planetary motion data, could a computer determine if the Solar System was geocentric or heliocentric? 
excerpt_separator: <!--more-->
---

There is a lot of interest in whether or not scientists can be assisted by AI and machine-learning methods to develop new scientific theory. I'd like to take a moment to illustrate how universality, which is one of the major advantages of deep-learning models, is also a detriment when it comes to knowledge discovery. 

Suppose that we were to provide a machine-learning algorithm with all the planetary motion data from Tycho Brahe. As you may know, Tycho Brahe's careful measurement of planetary data played a central role in the development of Kepler's laws, which in turn played a central role in Newton's theory of gravitation. The theory of gravitation gave a compelling physical mechanism that rationalized Copernicus' heliocentric model, versus the prevailing geocentric model. 

The heliocentric model is so obviously engrained in our intuition that it might seem obvious that a computer would pick the heliocentric model. But you might be surprised to learn that both the heliocentric and the geocentric model can describe planetary motion fairly well. 

![Retrograde Motion](/assets/img/blog/Retrograde.PNG){:data-width="1419" data-height="905"}
{:.figure}

Perhaps the most challenging phenomena to describe within the Geocentric model is the observation of Retrograde Motion, where planets actually backtrack briefly during their trajectory across the sky. Remember that Ptolemy, who came up with a geocentric model, was not a stupid guy. The geocentric model can accurately describe planetary motion because it operates based on a theory of epicycles. In the epicycle description, the planets do not just move on circles, but actually they move on circles around circles. Also the first circle is not centered at Earth but is slightly off centered. If you use epicycles, we can accurately predict planetary trajectories for several hundred years! In fact mechanical projectors in old planetariums operate using the geocentric description of the solar system. 

The reason epicycles work well is because they are Fourier series, which can approximate *any* smooth function. At the end of the day, Ptolemy's geocentric model is essentially a two-term Fourier series. If we add more terms to the Fourier series, we can describe any smooth function -- for example, here is another epicycle for my new institution, the University of Michigan: 

![MichiganEpicycle](https://media.giphy.com/media/kEd462ltfjjQ7b0Mvv/giphy.gif){:data-width="700" data-height="700"}
{:.figure}

Many of the powerful tools that are driving the AI revolution, such as deep-learning / neural networks, are also universal function approximators. I have no doubt that a neural network could also predict planetary trajectories with high fidelity. The problem is that in this case, you are getting the 'right answer' for the 'wrong reason'. 

From a trajectory prediction perspective, the heliocentric model and the geocentric model provide similar value. So why does a scientist benefit from the heliocentric model? The heliocentric model is a *structural form* that gives rise to the *physical mechanism* of gravity. The mechanism of gravity provides a deep conceptual foundation for us not only to interpret planetary motion, but also apple-earth interactions (a la Newton). It is these deep, transferrable conceptual frameworks that form the intuition which scientists value so much. 

![Ptolemy_vs_newton](/assets/img/blog/Ptolemy_vs_newton.PNG){:data-width="1419" data-height="905"}
{:.figure}


Our physical intuition is based on the structural form of knowledge representation. The contrast is that a machine-learned regression/classification model, for example, like the Epicycles, can provide accurate predictions, but it can be challenging to discover any insight from the Fourier Series. 

Let me conclude with one more example that is closer to chemistry and materials science. 

Here is a t-SNE representation of the elements, constructed from Word Embeddings of the Scientific Literature (Tshitoyan et al., [Nature 2019](https://www.nature.com/articles/s41586-019-1335-8). 

![PeriodicTable](/assets/img/blog/periodic_tnse-vs-mendeleev.PNG){:data-width="1419" data-height="905"}
{:.figure}

Let me start off by saying that this t-SNE representation is actually very awesome. It is spectactular that a computer can read through millions of abstracts and construct, just from word embeddings, a representation that actually does quite well in clustering the elements in sensible ways. 

My question though is, if we *did not* know the Periodic table, in other words, if there were no colorful markers that distinguished the elements into existing classifications, and we were just presented with black dots for each data point, would we be able to tease out the structural form of the elements from this t-SNE plot? My guess is no. And to me, the main reason is that the x- and y- axes in a t-SNE figure do not have any meaningful interpretation. Euclidean distances in this figure also do not have a real physical interpretation. Our appreciation of the clustering is post-hoc; we only appreciate that the t-SNE figure captures our existing intuition regarding the elements. 

In contrast, let's discuss Mendeleev's Periodic Table. The Periodic Table is actually a very unique structural representation. It is not a scatterplot, it is not a clustered dendrogram, nor is it some ranked list. 

When Mendeleev first created the Periodic Table, the organization was very phenomenological. Mendeleev started with the ansatz of Periodicity, and it was based on that structure that the first periodic table was made. Of course as time proceeded, the periodic table gained a more precise and also peculiar structural form; the first row has two elements, the next two rows have eight, the next two rows have eighteen elements; and the next two rows have 32 elements. 

As we today know, the structural form of the Periodic Table derives from the underlying s,p,d,f nature of the quantum-mechanical atomic orbitals. Not only did this heuristic representation of the Periodic Table accurately reflect underlying physics, this structural representation further led to the prediction of missing elements, which were later confirmed. 

Because the Periodic Table reflects the underlying quantum mechanical structure of elements, it also provides tremendous utility in interpreting chemistry. As any first year chemistry student knows, the structural form of the Periodic Table can be navigated to make arguments about electronegativity, atomic radius, metallic/ionic/covalent character, etc. This is the representation that produces true value. 

To conclude; much like the heliocentric structure of the solar system, and the periodic table, we interpret our world and universe from conceptual models. Many of these conceptual models have unusual structural form, and as far as I'm aware, this structural representation is not something that could pop out of any existing Machine-Learning package. From an engineering perspective, perhaps all we need is a good prediction. But like the Epicycle/Geocentric model of the Solar System, a prediction of where Jupiter is going to be in 22.45 years may have great engineering value, but it does not provide an intuitive conceptual understanding of gravity, which has great scientific value. 

In my opinion, the great challenge to us computational scientists will be to go beyond what is easy to obtain from machine-learning models, and be more deliberate about building models that capture the true structural form of Nature's representations. 

One last statement; there may not necessarily be a *ground-truth* in a structural representation. What makes a good representation? I think that it is just the utility that it provides a scientist. The greater the utility, the better the representation. This is why we must distinguish any big-data problem into two parts, a data exploration phase, where we seek to understand and interpret our data. Then the next stage, which can be even more difficult than the exploration stage, is to find compelling visualizations that communicate our learned intuition in informative and pedagogical ways. I think this is the major challenge of the data-driven scientist. 

For further reading on structural forms, here is a beautiful and very inspiring PNAS paper titled, [The Discovery of Structural Form](https://www.pnas.org/content/105/31/10687). 