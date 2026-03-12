# The Operational Acoustic–Affective Space (OAAS): A Framework for the Design and Evaluation of Functional Affective Sound Environments

**Maria Camila Ceballos**¹,*, **Juliana Zapata-Cardona**² and **Berardo de Jesús Rodríguez**²

¹ Faculty of Veterinary Medicine, University of Calgary, Clinical Skills Building,  
11877-85th Street NW, Calgary, AB T3R 1J3, Canada;  
<mariacamila.ceballos@ucalgary.ca>  

² Grupo de Investigación Patobiología QUIRON, Escuela de Medicina Veterinaria,  
Universidad de Antioquia, Calle 70 No. 52-21, Medellín 050010, Colombia;  
<juliana.zapata9@udea.edu.co> (J.Z.-C.); <berardo.rodriguez@udea.edu.co> (B.J.R.)  

\* Correspondence: <mariacamila.ceballos@ucalgary.ca>

## Abstract

Sound plays a fundamental role in shaping emotional, behavioral, and physiological states in living systems. Despite growing evidence that both animals and humans respond affectively to sound, most research still relies on exposure-based paradigms using pre-existing human music and lacks structured, translational methodologies for designing and evaluating sound-based interventions—particularly in animal models, where affective state must be inferred from objective indicators. Consequently, the relationship between acoustic structure and affective modulation remains poorly formalized, limiting reproducibility and cross-study comparability.

This study introduces the Operational Acoustic–Affective Space (OAAS) as a framework for the design and evaluation of affective sound environments. OAAS formalizes a shared coordinate space in which sound environments can be positioned, compared, and intentionally modified according to affective and regulatory objectives. Rather than prescribing specific musical strategies, OAAS provides an operational geometry derived from objective acoustic descriptors and empirically grounded affective anchors, enabling interpretable analysis across heterogeneous sound sources (e.g., functional music stimuli, vocalizations, and control noises).

OAAS is demonstrated through a set of porcine-centered case studies that illustrate three complementary functions: (i) establishing a biologically grounded acoustic–affective reference baseline using the SoundWel porcine vocalization corpus; (ii) situating a previously validated veterinary functional music program within this space for post-hoc structural interpretation; and (iii) demonstrating OAAS operability via directed acoustic transformations that produce measurable displacement toward predefined affective reference regions. These applications show how OAAS supports design-oriented reasoning and quantitative evaluation without reducing affective meaning to categorical labels.

OAAS is proposed as a foundational and extensible framework for affective sound environment science, bridging acoustic analysis, operational design, and evaluation within a unified methodological domain, and providing a transferable basis for future work integrating behavioral, physiological, and context-specific validation.

**Keywords:** animal vocalizations; animal welfare; bioacoustics; dimensional modeling; functional music; principal component analysis; sound design 

**Abbreviations:**
OAAS, Operational Acoustic–Affective Space; PCA, Principal Component Analysis; PC, Principal Component; STFT, Short-Time Fourier Transform; LUFS, Loudness Units relative to Full Scale; EBU R128, European Broadcasting Union Recommendation R128; SPL, Sound Pressure Level; HRV, Heart Rate Variability; QBA, Qualitative Behaviour Assessment; ILPP, Intrinsic, Listener, Playback and Producer-related assumptions; POS, Positive-directed transformation; NEG, Negative-directed transformation.

## 1. Introduction

The design of synthetic acoustic environments is an emerging applied field concerned with understanding and shaping how sound structures influence emotional, behavioral, and physiological states in living systems. Unlike isolated auditory stimuli, synthetic acoustic environments are conceived as structured, time-extended sound systems designed to modify the perceptual and affective context in which organisms are immersed, consistent with the soundscape paradigm and its operational definitions [@ISO12913_1_2014_Soundscape]. In recent years, synthetic sound environments have also gained relevance in computational acoustics and auditory research as controllable systems for simulating complex soundscapes and producing synthetic datasets for sound event detection, monitoring, and transfer learning [@ViverosMunozEtAl2023_SPASS; @LukashevichEtAl2023_PosteriorProbabilitiesMusicClassification].

Although existing soundscape standards and affective appraisal frameworks provide essential conceptual foundations for describing and measuring how environments are perceived, they rarely provide a unified operational geometry that supports intervention-oriented design and reproducible navigation across heterogeneous sound environments [@ISO12913_1_2014_Soundscape; @HerranzPascual2020_SoundscapeEmotionsReview]. In particular, there remains no operational coordinate framework that allows heterogeneous sound environments (e.g., functional music interventions, vocalizations, ecological soundscapes, and control noises) to be placed in a shared space and manipulated through explicit geometric operations—such as centroids, distances, trajectories, and displacement—under standardized acoustic representations. As a result, sound-based interventions are often treated as ad hoc exposures rather than controllable affective systems, limiting reproducibility, cross-study comparability, and the capacity to formalize “target states” and quantify directed change.

Despite extensive evidence that animals and humans exhibit emotional and physiological responses to sound, the field still lacks translational, design-oriented methodologies that connect acoustic structure with affective modulation in a reproducible way—particularly in animal models, where affective state must be inferred from objective indicators rather than verbal report [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @FiebigEtAl2020_EmotionTheorySoundscape]. Most studies remain exposure-based and frequently rely on pre-existing human music (often Western repertoires), reporting heterogeneous outcomes while providing limited mechanistic insight into which acoustic properties drive regulation, engagement, or aversion [@WellsGrahamHepper2002_DogsShelter; @KoganEtAl2012_KenneledDogs]. Moreover, methodological constraints remain a persistent barrier in animal-centered music research, where controlled experimentation, acoustic standardization, and species-appropriate interpretation are often limited [@Snowdon2021_AnimalsSignalsMusicWellBeing]. In addition, many approaches to “emotion in music” rely strongly on subjective self-report paradigms that are not directly portable to non-human contexts, reinforcing the need for frameworks that can operate with objective acoustic structure and organism-level inference when working across species [@FiebigEtAl2020_EmotionTheorySoundscape; @HerranzPascual2020_SoundscapeEmotionsReview].

Recent evidence from commercial farms suggests that functional veterinary music can improve maternal behavior and reduce piglet mortality during lactation [@MontoyaZuluaga2025_SciRepSowsInPress]. Yet such findings remain difficult to formalize and compare across contexts because interventions are rarely positioned relative to standardized baseline soundscapes or evaluated through a shared operational coordinate space. This limitation is especially relevant under real-world production conditions, where acoustic context is dynamic, uncontrollable, and often dominated by complex background noise, making it essential to define frameworks capable of quantifying baseline-to-intervention shifts and comparing different acoustic strategies under a common representation.

This paper addresses this gap by introducing the Operational Acoustic–Affective Space (OAAS), an applied framework for the analysis, design, and evaluation of synthetic acoustic environments conceived as functional affective systems. OAAS does not prescribe a specific acoustic or musical strategy. Instead, it provides a structured coordinate space in which acoustic environments can be positioned, compared, and systematically modified according to affective and regulatory objectives, enabling explicit representation of both baseline states and intentional transformations [@ZapataCardona2022_SciRepGrowingPigs; @ZapataCardona2023_SciRepSpectroTemporal; @ZapataCardona2024_SciRepMusicProgram].

In this study, the term synthetic acoustic environments refers to intentionally constructed soundscapes designed to shape the affective and regulatory conditions of a living system. These environments are conceived as structured acoustic ecosystems in which spectral, temporal, dynamic, and spatial properties interact over time to generate coherent perceptual and affective contexts, consistent with the foundational soundscape tradition [@Schafer1977_TheSoundscape; @Truax2001_AcousticCommunication] and with standard soundscape conceptualizations [@ISO12913_1_2014_Soundscape]. OAAS adopts this ecological–systemic view of sound and extends it into an operational framework that enables synthetic environments to be quantitatively positioned, compared, and modified within a shared acoustic–affective coordinate space.

Within this framework, music is treated as one possible implementation of a synthetic acoustic environment rather than a privileged category. While music represents a culturally formalized mode of sound organization in humans, musicality can be understood more broadly as an adaptive capacity for structuring acoustic patterns in ways that modulate attention, arousal, and affective meaning [@HoningEtAl2015_PhiloTransMusicality; @Fitch2015_PhiloTransBioMusicology]. Accordingly, music is conceptualized here as an intentional soundscape: a constructed acoustic micro-ecosystem whose organization can evoke ecological resonance without requiring direct imitation of vocal expressions [@Schafer1977_TheSoundscape; @Truax2001_AcousticCommunication]. This perspective also clarifies the role of vocalizations in the present work: auditory perception is not adapted to vocal communication alone, but to the broader acoustic structure of ecosystems in which vocalizations function as biologically meaningful signals embedded within environmental soundscapes. Vocalizations are therefore used here not as musical templates, but as ecologically grounded affective anchors for defining OAAS reference regions.

The development of OAAS is grounded in more than a decade of empirical research using animal models, where sound-based interventions—including veterinary functional music—were designed, deployed, and validated under controlled conditions [@ZapataCardona2022_SciRepGrowingPigs; @ZapataCardona2023_SciRepSpectroTemporal; @ZapataCardona2024_SciRepMusicProgram]. In the present study, this empirical foundation is not revisited experimentally; rather, it is used to formalize an operational acoustic–affective design space and to demonstrate how biologically grounded vocal reference signals (porcine vocalizations) can be used to structure and interpret synthetic acoustic environments within a shared coordinate domain [@BrieferEtAl2022_SciRepSoundWel].

The objective of this study is to formalize OAAS as a reproducible and extensible framework that enables synthetic acoustic environments to be represented, compared, and intentionally navigated within a low-dimensional acoustic–affective space, supporting systematic evaluation and directed displacement toward predefined affective reference regions.


## 2. Materials and Methods

This section describes the methodological basis of the proposed framework. Rather than presenting a single experimental protocol, it outlines the conceptual design principles, analytical tools, and evaluation strategies that constitute the Operational Acoustic–Affective Space (OAAS), drawing on a body of empirical work conducted across multiple studies and applied contexts.

### 2.1. Conceptual and Applied Background

Research on sound and music in biological systems has traditionally emphasized exposure-based approaches, in which organisms are presented with predefined auditory stimuli and their responses are subsequently measured. In animal research, this has most often involved the use of human music repertoires—particularly Western classical music—applied across species and contexts with variable and sometimes contradictory outcomes [@AlworthBuerkle2013_MusicAnimalPhysiologyWelfare]. While such studies demonstrate that sound can influence behavior and physiology, they provide limited insight into how specific acoustic structures relate to emotional processing, or how acoustic environments should be intentionally designed.

A notable methodological advance was introduced by Snowdon and Teie through their proposal of species-specific music [@SnowdonTeie2010_TamarinsSpeciesMusic; @SnowdonTeieSavage2015_CatsSpeciesMusic]. Their work derived musical stimuli from species-typical vocalizations by transforming vocal signals into symbolic representations rendered through instrumental timbres. Behavioral validation emphasized affiliative responses, demonstrating that vocal-derived acoustic material can modulate emotional engagement.

Despite its relevance as an early biologically grounded strategy, species-specific music presents limitations when considered as a general framework for affective acoustic intervention. By treating vocalizations primarily as generative templates, such approaches can constrain design to narrow affiliative functions and limit broader ecological or contextual relevance. Moreover, species-specific methods do not explicitly address how different affective states might be targeted, compared, or evaluated across time and environments.

More recent theoretical and interdisciplinary perspectives emphasize integrating animal perception, emotional evaluation, and welfare objectives into the study of music and sound [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. These contributions clarify key challenges, including heterogeneity of experimental designs and the persistent lack of mechanistic links between acoustic structure and affective outcomes. However, many proposals remain primarily conceptual, providing limited operational guidance for systematic analysis, design, and evaluation of sound environments as functional systems.

In parallel, our group has approached sound-based interventions from an emotion-centered experimental perspective. Rather than starting from predefined acoustic forms, we investigated how variations in sound structure, timbre, and temporal organization elicit differentiated emotional responses—initially characterized through qualitative behavioural assessment (QBA) and later through physiological and production-related indicators [@ZapataCardona2022_SciRepGrowingPigs; @ZapataCardona2023_SciRepSpectroTemporal; @ZapataCardona2024_SciRepMusicProgram]. This work treated sound not as a stimulus category, but as a multidimensional affective substrate whose properties can be analyzed, manipulated, and deployed over time.

A central point of convergence across these approaches is the recognition that vocalizations contain rich emotional information [@Briefer2012_VocalExpressionEmotionsMammals; @LaurijsBrieferReimertWebb2021_FarmAnimalVocalisationsPositiveWelfare; @SnowdonTeieSavage2015_CatsSpeciesMusic]. However, in OAAS we argue that vocal signals should not be copied or directly translated into musical material. Instead, they must be analytically decomposed to identify the spectral, temporal, and dynamic features that convey affective meaning. Emotional content emerges from the organization of these features, not from vocal form reproduction.

From this perspective, strict species-specificity is not a prerequisite for affective acoustic design. Perceptual and emotional systems involved in sound interpretation share conserved functional principles across mammals, reflecting shared evolutionary pressures to decode acoustic environments [@ZapataCardona2024_AnimalsReview]. This conservation supports the development of synthetic acoustic environments that maintain ecological validity while allowing controlled manipulation of affect-relevant parameters.

These considerations motivate the need for a formal framework capable of integrating acoustic analysis, emotional evaluation, design decision-making, and quantitative assessment. In the following section, we introduce the Operational Acoustic–Affective Space (OAAS) as an applied framework that formalizes synthetic acoustic environments as both analytical and design spaces for affective sound-based interventions.


### 2.2. Definition of the Operational Acoustic–Affective Space (OAAS)

The Operational Acoustic–Affective Space (OAAS) is defined as a formal framework for representing, analyzing, and designing sound-based environments according to their affective impact on living systems. OAAS conceptualizes sound not merely as a physical signal or aesthetic artifact, but as an organized acoustic substrate capable of eliciting emotional, behavioral, and physiological responses. Within this framework, synthetic acoustic environments are treated as systems whose properties can be described, manipulated, and evaluated in relation to affective regulation.

The term operational indicates that OAAS is defined through measurable and actionable variables derived from sound and organismal responses, rather than from subjective self-report. Affective dimensions are therefore constructed from objective acoustic, behavioral, and physiological metrics, enabling their application in animal models and other contexts where verbal access to emotional states is unavailable.

The acoustic–affective space refers to a low-dimensional representation in which affect-relevant properties of sound and organismal responses can be jointly examined. Although the geometric structure of this space may resemble affective representations such as valence–arousal models, OAAS does not assume predefined emotional categories. Instead, affective dimensions emerge from the organization and clustering of measured variables, allowing comparisons across conditions, time scales, and intervention strategies.

In the present study, OAAS is operationalized as a three-dimensional coordinate space derived from the first three principal components (PC1–PC3) of a standardized acoustic feature set. Principal component analysis is used as an explicit acoustic coordinate system in which sound environments can be positioned, compared, and systematically designed. While low-dimensional projections are used for visualization, OAAS-based quantitative analyses are performed in the full three-dimensional space.

Within OAAS, each acoustic environment is represented as a region or trajectory, reflecting its structural properties and functional effects. Musical compositions, vocalizations, ecological soundscapes, mechanical noise, or hybrid acoustic systems can all be positioned in the same analytical space, provided that relevant acoustic and response metrics are available.

### 2.3. OAAS Design Parameters

Within the OAAS framework, synthetic acoustic environments are defined and manipulated through a set of design parameters describing how sound is structured, delivered, and experienced over time. Parameters do not prescribe specific sound sources or aesthetic forms; instead, they characterize affect-relevant acoustic properties that can be systematically analyzed and controlled.

For operational purposes, OAAS parameters are organized into four interrelated domains: spectral, temporal, dynamic, and informational.

(i) Spectral domain.
Spectral parameters describe frequency-related properties such as bandwidth, spectral centroid, spectral slope, harmonicity, and energy distribution across bands. Spectral configuration determines perceptual salience and biological accessibility, and relates to timbral qualities and similarity to natural vocal or ecological sound patterns.

(ii) Temporal domain.
Temporal parameters characterize event timing, rhythmic organization, tempo and pulse regularity, temporal density, and modulation rates. Temporal structure influences predictability, entrainment, attention, and arousal regulation across exposure regimes.

(iii) Dynamic domain.
Dynamic parameters describe amplitude-related behavior over time, including sound level, dynamic range, onset and decay profiles, and amplitude modulation. Dynamic control shapes energetic profiles and supports avoidance of overstimulation in long-term exposures.

(iv) Informational domain.
Informational parameters capture higher-level organization such as complexity, variability, redundancy, novelty, and structural coherence. This domain is relevant for distinguishing neutral, enriching, and disruptive environments and for supporting stability or exploratory engagement.

Integration of domains.
OAAS treats these domains as integrated, not independent. Each synthetic acoustic environment corresponds to a configuration in this multidimensional parameter space, which can be analyzed directly or projected into low-dimensional OAAS coordinates. This integration supports: (i) comparative analysis; (ii) identification of parameter ranges linked to affective outcomes; and (iii) design decision-making via controlled transitions in OAAS.

### 2.4. Acoustic and Musical Design Pipeline

Within OAAS, the production of synthetic acoustic environments is conceived as a design process guided by affective objectives rather than by predefined aesthetic categories. OAAS links diagnostic analysis, design decision-making, and post-production evaluation within a shared acoustic–affective space.

(i) Contextual diagnosis.
A baseline acoustic context is characterized (vocalizations, environmental sound, or existing interventions). OAAS parameters identify dominant spectral, temporal, dynamic, informational, and spatial features. Output: a reference region in OAAS.

(ii) Target definition.
A target region is defined based on objectives such as stress reduction, affiliative engagement, or arousal modulation. Target definition constrains parameter selection.

(iii) Iterative design decisions.
Sound production proceeds through controlled modifications in OAAS parameter space. In musical design: instrumentation, timbre, harmonic density, rhythmic structure, dynamics, and pacing. In non-musical/hybrid design: source selection, layering, noise shaping, spatial diffusion.

(iv) Post-production OAAS verification.
Stimuli are analyzed and projected into OAAS to verify alignment with the intended target. Discrepancies inform iterative refinement.

Spatial configuration is treated as an integral design component: diffusion, movement, and positioning influence perceptual integration, affecting OAAS positioning depending on playback conditions.

| Pipeline Stage | OAAS Function | Analytical Basis | Design Actions | Output |
|---|---|---|---|---|
| Contextual diagnosis | Characterize initial acoustic–affective state | Acoustic metrics, vocalization analysis, baseline environmental sound | Identify dominant spectral, temporal, dynamic, informational, and spatial features | Reference region in OAAS |
| Affective objective definition | Define target acoustic–affective region | Behavioral goals, regulatory needs, contextual constraints | Prioritize OAAS domains and desired ranges | Target region in OAAS |
| Design strategy selection | Select intervention approach | Comparison between initial and target regions | Decide on musical, non-musical, hybrid, ecological, minimalist strategies | Design pathway |
| Sound production | Navigate OAAS | Parameter-guided design decisions | Timbre, temporal structure, dynamics, spatial deployment | Candidate acoustic environment |
| Post-production analysis | Verify OAAS positioning | Feature extraction + OAAS projection | Compare produced vs. target region | Evaluated configuration |
| Iterative refinement | Reduce discrepancy | Target vs observed comparison | Parameter adjustment and redesign | Finalized environment |
| Deployment + evaluation | Assess functional impact | Behavioral, physiological, contextual indicators | Exposure protocols + outcome assessment | Validated intervention |

Detailed production protocols and implementation examples used across OAAS-based interventions are provided as Supplementary Material.

### 2.5. Evaluation Methodology

All musical stimuli were converted to mono, resampled to **48 kHz**, and loudness-normalized to **−23 LUFS** following the **EBU R128** standard prior to feature extraction. This ensured acoustic comparability across musical stimuli and with the SoundWel-derived porcine vocalization baseline.

Evaluation in OAAS is conceived as a multi-level process assessing synthetic acoustic environments as **functional affective systems** rather than isolated stimuli. OAAS integrates evaluation into the same acoustic–affective space used for diagnosis and design, enabling coherent comparisons between natural vocal expressions, designed sound environments, and control stimuli.

Evaluation operates across three interrelated levels: **(i) acoustic verification**, **(ii) organismal response evaluation and affective anchoring**, and **(iii) contextual/functional outcomes**.

#### 2.5.1. Acoustic verification

Each produced sound environment is analyzed using the same OAAS parameter domains employed during design. Stimuli are projected into the OAAS to confirm their positioning within the intended region. This step supports reproducibility and interpretation of subsequent analyses.

In addition, to define a biologically grounded OAAS reference baseline, porcine vocalizations from the SoundWel database were processed to enable direct comparison with longer-duration designed acoustic environments (e.g., musical stimuli). Because individual vocalizations are short and locally variable, recordings were aggregated into category-specific macrosegments of approximately **3 min**, preserving contextual specificity while providing time-extended acoustic profiles comparable in scale to intervention stimuli.

For each macrosegment, acoustic descriptors spanning the OAAS parameter domains (**spectral, temporal, dynamic, and informational**) were extracted following the standardized feature pipeline described above. Features were subsequently **z-score normalized** using the same reference scaling applied to all sound environments included in the OAAS, ensuring comparability between vocalization-derived baselines, musical stimuli, and control sounds.

Normalized feature vectors were projected into the OAAS defined by the **first three principal components (PC1–PC3)**. Vocalization categories were represented as regions in the OAAS and summarized by their **centroids** and dispersion profiles. These vocalization-derived regions function as biologically grounded affective reference anchors for subsequent post-hoc evaluation and distance-based analyses of designed sound environments (Sections **3.2–3.3**).

#### 2.5.2. Organismal response evaluation and affective anchoring

In animal models, organismal evaluation relies on behavioral and physiological indicators reflecting affective state without verbal report. Behavioral indicators include **QBA-derived descriptors**, ethological observations, affiliative/agonistic interactions, activity patterns, environmental use, and stress-related behaviors. Physiological indicators may include autonomic measures (e.g., **HRV**), endocrine markers, or production-related outcomes depending on the applied context.

Within OAAS, organismal response evaluation serves two complementary functions: **(i)** providing an empirical basis for anchoring acoustic regions to biologically meaningful affective contexts, and **(ii)** supporting validation of designed environments when experimental response measures are available. Importantly, the present study does not introduce new behavioral or physiological experiments; instead, OAAS is anchored through biologically grounded affective reference contexts derived from previously validated sources.

Affective anchoring is established primarily through porcine vocalization categories extracted from the SoundWel database, a corpus of vocal signals emitted under well-defined production contexts with affect-related descriptors assigned by the original authors. These vocalizations function as natural affective reference regions in OAAS, enabling the space to be populated with biologically meaningful acoustic configurations associated with affiliative/positive contexts, high-activation exploratory states, baseline regulatory conditions, transient uncertainty-related events, and sustained negative contexts.

To reinforce interpretability and maintain methodological continuity with previous intervention studies, SoundWel context categories were conceptually aligned with QBA-based affective descriptors used in veterinary functional music research. While SoundWel provides emission-context categories rather than QBA ratings per se, both frameworks converge in their objective: describing affective state through observable behavioral and contextual correlates. This linkage supports an interpretable mapping between naturally expressed affective communication and intervention-oriented affective modeling, without assuming categorical equivalence.

Crucially, OAAS interpretation avoids assuming that acoustic similarity implies equivalence of emotional experience. Instead, proximity within OAAS is interpreted as **graded structural alignment**: acoustic configurations may resemble those of affectively grounded vocal contexts while differing in emotional meaning due to environment, perception, and functional role. Therefore, acoustic convergence must be interpreted in relation to context descriptors and, when available, behavioral validation.

This anchoring strategy also supports a methodological shift in welfare-oriented acoustics. Whereas many welfare studies prioritize the detection of distress-related states, OAAS explicitly enables the identification and operational use of **positively valenced acoustic regions**, supporting intervention design aimed at calm, affiliative engagement, and resilience—not merely the reduction of negative conditions.

**Table 2. Conceptual alignment between SoundWel context categories and QBA-derived affective descriptors used in OAAS intervention research.**

| SoundWel vocalization context (emission conditions) | Indicative affective context (SoundWel descriptors) | Closest QBA-oriented affective descriptors (OAAS framework) | Interpretation notes for OAAS anchoring |
|---|---|---|---|
| Social affiliative / contact contexts | Positive / low–moderate activation | Calm, relaxed, content, affiliative | Positive reference core; emphasizes stability and low irregularity. |
| Exploratory / active engagement contexts | Positive or neutral / high activation | Curious, active, engaged, playful | High activation without distress; supports enrichment-oriented anchoring. |
| Baseline / routine neutral contexts | Neutral / low activation | Neutral, regulated, stable | Regulatory baseline; neutrality is treated as a meaningful state, not absence of affect. |
| Social separation / transient uncertainty contexts | Negative or mixed / moderate activation | Alert, uneasy, tense, uncertain | Transitional states; anchoring emphasizes ambiguity and context dependence. |
| Restraint / handling stress contexts | Negative / high activation | Anxious, distressed, agitated | High irregularity + high activation reference; interpreted cautiously as structural alignment only. |
| Acute nociceptive contexts (e.g., castration) | Negative / very high activation | Acute distress, panic-like agitation | Extreme high activation negative contexts; used as boundary region in OAAS. |

*Important note: This table represents a conceptual anchoring strategy for interpretability, not categorical equivalence. OAAS proximity indicates structural alignment of acoustic configuration rather than direct emotional identity.*

#### 2.5.3. Contextual and functional outcomes

The third level considers contextual and functional outcomes such as health, productivity, social stability, environmental use, or task performance. These outcomes link affective modulation to system-level effects, especially under long-term exposure scenarios. Within OAAS, they are interpreted as emergent consequences of sustained interaction between organisms and acoustic–affective configurations.

#### 2.5.4. OAAS-based geometric analyses (centroids, distances, and displacement)

Quantitative evaluation within OAAS is performed using geometric analyses in the acoustic–affective space rather than hypothesis-driven inferential statistics.

Each acoustic segment or stimulus is represented by its OAAS coordinates in three dimensions:

$$
\mathbf{x} = (PC1, PC2, PC3)
$$

For a region (cluster) containing $N$ segments, the centroid is computed as:

$$
\mathbf{c} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{x}_i
$$

Similarity and separation between configurations are quantified using Euclidean distance in three dimensions:

$$
d(\mathbf{x}, \mathbf{c}) = \sqrt{(x_1-c_1)^2 + (x_2-c_2)^2 + (x_3-c_3)^2}
$$

Directional change resulting from OAAS-guided design is expressed as a displacement vector:

$$
\Delta \mathbf{x} = \mathbf{x}_{final} - \mathbf{x}_{initial}
$$

Two-dimensional projections are used exclusively for visualization and do not enter quantitative evaluation.

**Table 3. OAAS geometric descriptors used for quantitative comparison and operability assessment.**

| Descriptor | Definition | OAAS interpretation | Use in this study |
|---|---|---|---|
| OAAS coordinate ($\mathbf{x}$) | Stimulus position in (PC1–PC3) | Acoustic–affective configuration | Represents vocalization clusters, musical stimuli, and controls |
| Centroid ($\mathbf{c}$) | Mean coordinate of a group/region | Reference region (affective anchor) | SoundWel clusters and program families |
| Distance $d(\mathbf{x},\mathbf{c})$ | Euclidean distance (3D) | Structural proximity | Quantifies similarity to affective reference contexts |
| Displacement $\Delta \mathbf{x}$ | Vector between configurations | Directed navigation | Used to evaluate OAAS operability and directed transformations |
| Distance change $\Delta d$ | Difference in distance across transformations | Improvement/constraint | Captures asymmetry in navigability |

#### 2.5.5. Iterative evaluation and reproducibility

Evaluation within OAAS is iterative. Discrepancies between intended and observed acoustic–affective configurations inform subsequent adjustments in design parameters, exposure strategies, or spatial deployment. By expressing evaluation in explicit coordinates, centroids, and distances, OAAS supports transparent comparison and reproducible refinement across studies.


## 3. Results

This section presents a set of selected applications and case studies illustrating how the OAAS framework can be operationally applied to characterize, interpret, and compare acoustic environments in animal-centered contexts. Rather than reporting new behavioral or physiological experiments, these case studies focus on the structural behavior of the acoustic–affective space when populated with natural vocal expressions and designed sound environments.

The analyses presented here demonstrate how OAAS functions as an integrative framework that links diagnostic acoustic baselines, post-hoc evaluation of previously validated interventions, and inter-species comparison within a common representational space. Each case study applies the methodological principles described in Section 2.5 to empirically grounded datasets, highlighting how affect-relevant acoustic structure can be examined across different sound sources and temporal scales.

Together, these applications serve as a proof of concept for OAAS as a design- and evaluation-oriented framework. They establish a foundation for interpreting subsequent quantitative results and for extending OAAS to additional species, sound environments, and applied domains.

## 3.1. Porcine Vocalizations as an OAAS Diagnostic Baseline

As a first case study, the OAAS framework was applied to porcine vocalizations to establish an acoustic–affective reference baseline grounded in natural emotional expression. Vocal communication constitutes a primary channel for affective signaling in pigs and has been widely studied as a source of biologically meaningful acoustic information. The SoundWel pig vocalization database provides a comprehensive and publicly documented corpus of vocal signals recorded across diverse production contexts, offering a valuable reference for welfare-oriented acoustic research.

In the SoundWel project, vocalizations were collected across multiple emission contexts and accompanied by ethologically grounded contextual annotations, including conditions associated with positive- versus negative-related welfare contexts. This corpus demonstrates that pig vocal signals contain structured acoustic information that can be leveraged for context-aware interpretation and welfare-related assessment. In the present study, we do not aim to replicate or validate the SoundWel classification strategy. Instead, we use the SoundWel database as a biologically grounded reference substrate to populate the OAAS and to define acoustic regions associated with distinct affect-relevant emission contexts.

This approach complements classification-oriented perspectives by providing an operational geometric representation in which affect-related acoustic configurations can be compared across heterogeneous sound sources. In other words, rather than predicting categories, OAAS formalizes a shared coordinate space that enables the positioning, comparison, and evaluation of designed acoustic environments relative to biologically grounded reference regions. Importantly, emission contexts are not used to shape the acoustic space, but to interpret the structure that emerges from acoustic features.

Porcine vocalizations were projected into the OAAS following the procedures described in Section 2. The resulting OAAS baseline reveals structured organization of vocalization-derived regions within the acoustic–affective space (Figure 1). Distinct regions emerge that correspond to affiliative/positive contexts, high-activation exploratory states, baseline regulatory conditions, transient uncertainty-related events, and sustained negative contexts. Importantly, these regions are not imposed through ad hoc assumptions, but emerge from the acoustic structure of the vocalizations in conjunction with independently defined emission contexts.

This vocalization-derived OAAS baseline serves two complementary functions. First, it provides a biologically grounded coordinate reference for situating designed sound environments intended for porcine contexts. Second, it supports structured comparison between natural vocal expression and synthetic acoustic environments, enabling evaluation of whether sound-based interventions occupy regions associated with regulatory, affiliative, exploratory, or aversive acoustic configurations. These functions form the basis for the post-hoc OAAS evaluation of a veterinary functional music program presented in the following section.




![](Outputs/Figures_OAAS/Figure_1_OAAS_baseline.png){width=90%}



Figure 1. OAAS baseline derived from porcine vocalizations.
Projection of aggregated porcine vocalization segments into the Operational Acoustic–Affective Space (OAAS). Panels show PC1 vs. PC2 (A) and PC1 vs. PC3 (B). Distinct regions emerge corresponding to different vocalization contexts, illustrating structured organization of biologically grounded acoustic signals within the OAAS.

## 3.2. OAAS-Based Post-Hoc Evaluation of a Veterinary Functional Music Program

As a second case study, the Operational Acoustic–Affective Space (OAAS) was applied as a post-hoc analytical framework to a previously validated veterinary functional music program developed for pigs. Rather than re-evaluating behavioral or physiological outcomes, this analysis focuses on the geometric positioning of the musical stimuli within the three-dimensional OAAS (PCA1–PCA3) defined by the porcine vocalization diagnostic baseline. This approach enables examination of the acoustic–affective structure of the program in relation to regions of the space populated by biologically grounded vocal reference contexts.

The functional music program was originally conceived as a structured acoustic intervention composed of multiple musical stimuli designed to modulate activity, social interaction, and environmental engagement under intensive housing conditions. While its design rationale, experimental protocol, and empirical validation have been reported elsewhere (Zapata-Cardona et al., 2024), the present analysis uses OAAS to situate the program acoustically, revealing how individual stimuli and the program as a whole relate to vocalization-derived reference regions that provide affect-relevant anchoring.

The OAAS was defined by the first three principal components derived from the standardized core acoustic feature set, which together explained 84.0% of the total variance (PC1 = 45.3%, PC2 = 28.7%, PC3 = 10.0%). PC1 was primarily driven by informational and spectrotemporal complexity metrics, including temporal entropy of the amplitude envelope, multiscale entropy, spectral entropy, and harmonic ratio. Higher PC1 values were associated with increased acoustic irregularity, reduced harmonic structure, and greater informational load, whereas lower values reflected more predictable, structured, and harmonic configurations. Within OAAS, PC1 is therefore interpreted as an operational axis of structured irregularity versus regulated organization, which is often consistent with contrasts observed between high-activation distress-like vocal structure and more stable affiliative or regulatory configurations. Importantly, this interpretation is structural rather than categorical: OAAS dimensions capture organized acoustic variation that may support, but does not determine, affective meaning.

The proportion of explained variance for PC1–PC3 and the cumulative variance are reported in Supplementary Table S2, and the corresponding variable loadings are provided in Supplementary Table S3.

PC2 was dominated by spectral flatness and entropy-dispersion descriptors, capturing differences in broadband noise content and spectral organization. Higher PC2 values corresponded to noisier, less tonally defined environments, while lower values indicated greater spectral organization. This component is interpreted as an activation–organization axis, distinguishing stimulating or exploratory acoustic environments from more constrained or monotonous ones. PC3, although accounting for a smaller proportion of variance, captured finer-grained variation related to harmonic balance and entropy distribution, enabling discrimination between acoustically similar stimuli occupying adjacent OAAS regions and supporting trajectory-based analyses of acoustic transformation.

A complete summary of the OAAS feature contributions to each component is provided in Supplementary Table S3.

Audio materials corresponding to the musical stimuli included in the functional program were analyzed using the same OAAS parameter domains applied to porcine vocalizations. Feature extraction and normalization followed established pipelines, ensuring that natural vocal expression, designed musical environments, and control stimuli were represented within a common analytical space. By treating the functional music program as an integrated acoustic system rather than as a collection of isolated pieces, OAAS provides a structured methodology for post-hoc evaluation that complements empirical behavioral and physiological assessments and informs future redesign.

Several musical stimuli designed as progressive variations of the same compositional strategy (W3_05, W5_05, W9_05) occupied virtually identical positions within the OAAS. These stimuli were intentionally conceived to present information gradually and repetitively, supporting activation, engagement, and resilience rather than aversion. Their convergence within the OAAS indicates that the framework captures functional acoustic organization rather than superficial musical identity. Although these stimuli were positioned near the vocalization-derived negative reference core, this proximity reflects shared structural features associated with high activation and spectral density, rather than the ethological context of distress. This distinction reinforces a key OAAS principle: geometric proximity indicates graded structural alignment and affective plausibility, but does not imply emotional identity.

Importantly, control noise stimuli did not systematically align with the vocalization-derived regions associated with sustained negative contexts. Although broadband and noisy by construction, these controls lacked the informational and dynamic organization characteristic of biologically grounded high-activation vocal structure. This supports the broader principle that affect-relevant acoustic organization depends on structured irregularity—including entropy-related dynamics—rather than broadband spectral content alone. In other words, noise per se is not necessarily aversive in species whose natural vocal communication is inherently noisy; what matters is how noise-like energy is organized temporally and informationally.

Notably, the positive anchor stimuli (W1_08, W10_08) were found to be compositionally and timbrally close to the negative anchor family (W3_05, W5_05, W9_05), differing primarily in parameter configuration rather than in musical identity. These stimuli were conceived as derived versions within the same compositional strategy, suggesting that the observed OAAS displacement reflects intentional modulation of acoustic parameters rather than a categorical change in sound type. This finding indicates that OAAS is capable of capturing directed acoustic transformations that align with compositional decisions made independently of the formal model, reinforcing its validity as an operational design space.

OAAS-based Euclidean distances between the music-derived sound environments and the OAAS-POS/OAAS-NEG reference centroids, along with their differential distance (Δ = dPOS − dNEG), are summarized in Supplementary Table S1.

The spatial distribution of musical stimuli, porcine vocalizations, and control sounds within the OAAS is shown in Figure 2. Musical stimuli occupy a constrained and structured region of the acoustic–affective space, partially overlapping with areas populated by porcine vocalization aggregates while remaining clearly separated from broadband control noise. This partial spatial convergence reflects similarity in acoustic organization rather than categorical equivalence. Musical points do not collapse into vocalization clusters, nor do they align systematically with control noise regions. Instead, they occupy intermediate OAAS regions characterized by structured temporal organization, controlled spectral density, and moderate informational complexity. This configuration is consistent with the intended functional design of the program, which sought to provide biologically meaningful acoustic stimulation without mimicking natural vocalizations or introducing unstructured noise.

Importantly, the visual overlap observed in the two-dimensional projections (PC1–PC2 and PC1–PC3) represents proximity in selected dimensions of the OAAS rather than full convergence across the three-dimensional space. As such, Figure 2 should be interpreted as illustrating graded acoustic–affective alignment rather than identity between designed musical environments and natural vocal expressions.




![](Outputs/Figures_OAAS/Figure_2_OAAS_overlay_clean.png){width=90%}



Figure 2. OAAS overlay of porcine vocalizations, functional music stimuli, and control sounds.
Projection of designed musical stimuli and control sounds onto the Operational Acoustic–Affective Space (OAAS) defined by porcine vocalizations. Musical stimuli occupy intermediate regions of the space, showing graded proximity to multiple vocalization clusters rather than categorical alignment. Control sounds remain structurally distinct, illustrating that broadband noise does not inherently map onto vocalization-derived regions associated with sustained negative contexts.

## 3.3. OAAS Operability: Directed Displacement of Musical Stimuli within the Acoustic–Affective Space

To evaluate the operability of the Operational Acoustic–Affective Space (OAAS) beyond descriptive representation, two musical stimuli from the veterinary functional music program (W7_01 and W8_03) were subjected to controlled acoustic transformations aimed at directed displacement toward predefined porcine vocalization-derived reference regions. Stimulus labels correspond to internal identifiers within the development program and are used here solely for traceability.

#### 3.3.1. Baseline Position of Musical Stimuli in OAAS

For each stimulus, baseline position within the three-dimensional OAAS was quantified by calculating Euclidean distances to vocalization-derived reference centroids representing positively and negatively annotated emission contexts (Section 2.5). These baseline distances served as reference values for evaluating transformation performance. Importantly, these reference regions provide biologically grounded anchors for operational comparison, not categorical affect labels: proximity indicates graded structural alignment with vocalization-derived acoustic configurations.

The two stimuli exhibited distinct initial configurations: while both occupied intermediate OAAS regions, W8_03 was initially located closer to the negatively annotated reference region compared to W7_01, indicating stimulus-dependent differences in baseline affect-relevant acoustic proximity.

#### 3.3.2. Directed Acoustic Transformations and Distance Modulation

For each stimulus, multiple candidate transformations were generated under controlled parameter constraints targeting displacement toward either the positive (POS) or negative (NEG) vocalization-derived reference centroid. From each candidate set, the variant yielding the minimal distance to the target centroid was selected for analysis.

Positive-directed displacement (POS).
For both W7_01 and W8_03, OAAS-positive transformations produced a reduction in distance to the positive reference region. For W7_01, the distance decreased from 16.73 to 16.61, and for W8_03 it decreased from 14.89 to 14.76. These results demonstrate that positive-directed navigation was achievable across distinct musical contexts.

Negative-directed displacement (NEG).
Negative-directed transformations exhibited stimulus-dependent behavior. For W7_01, the distance to the negative reference region decreased from 16.67 to 16.52, indicating effective displacement. In contrast, for W8_03, negative-directed transformations did not yield further distance reduction; instead, the best candidate increased the distance from 14.83 to 15.66.

#### 3.3.3. Asymmetry and Saturation Effects in OAAS Navigability

The contrasting behavior observed for negative-directed displacement highlights an asymmetry in the navigability of the acoustic–affective space. While positive-directed displacement was consistently achievable, negative-directed displacement appeared constrained for stimuli already positioned near the negative reference region.

For W8_03, the original stimulus was already located close to the negative vocalization-derived centroid, and further displacement was not achievable without violating established acoustic feature constraints. This behavior suggests region-specific saturation effects, indicating that OAAS navigation is not uniformly bidirectional across all regions of the space.

#### 3.3.4. Preservation of Musical Identity under OAAS-Guided Modulation

Across all transformations, the higher-level musical organization and temporal coherence of the stimuli were preserved. Directed displacement primarily affected fine-grained acoustic texture—local redistribution of spectral energy and temporal micro-structure—while leaving global structural identity intact. This demonstrates that OAAS-guided modulation can shift the functional sonority of a piece without reauthoring its musical structure, supporting OAAS as an operational calibration space for production-sensitive sound environments.

A key methodological implication is that the functional positioning of a stimulus can depend critically on production-level processes (e.g., spectral balance, timbral density, micro-dynamics), even when the underlying composition remains unchanged. This observation is especially relevant in animal-centered music research, where stimuli are often drawn from existing human repertoires without accounting for how recording, mixing, and mastering practices may substantially alter psychoacoustic structure—and therefore affective outcomes. OAAS provides a means of verifying and adjusting such production-sensitive configurations, enabling reproducible quality-control practices for sound-based interventions.

#### 3.3.5. Summary of OAAS Operability

Together, these results demonstrate that OAAS functions as an operable control space capable of supporting directed and quantifiable displacement of designed sound environments toward biologically grounded reference regions. At the same time, OAAS reveals intrinsic structural constraints and asymmetries that define feasible transformation boundaries—information that is critical for real-world affect-oriented sound environment design.




![](Outputs/Figures_OAAS/Figure_3_OAAS_transformations_multpanel_FINAL_300dpi.png){width=90%}



Figure 3. OAAS-directed transformations and multilevel acoustic displacement of two musical stimuli.
Multi-panel visualization of OAAS-guided positive (POS) and negative (NEG) transformations for W7_01 and W8_03. (A) Mel-spectrograms of the original stimuli and their selected POS/NEG variants. (B) Δ mel-spectrograms relative to the original (variant − original), highlighting local spectrotemporal redistribution. (C) Δ band-energy profiles (low/mid/high frequency bands) relative to the original. (D) OAAS displacement trajectories (PC1 vs. PC3), showing directed movement from the original point (black) toward the selected POS (green) and NEG (red) variants.

These findings suggest that OAAS may function not only as an evaluation space, but also as a production-sensitive calibration domain in which structurally coherent stimuli can be shifted toward targeted affect-relevant regions.

#### 3.3.6. Proximity of Musical Stimuli to Porcine Vocalization Categories

To further characterize the acoustic–affective positioning of the designed musical stimuli, Euclidean distances were computed between each musical item and the centroids of the porcine vocalization categories defined within the OAAS. This analysis quantifies which categories are acoustically closest to, and most distant from, each stimulus without invoking categorical emotional labeling.

Distance analysis revealed stimulus-specific patterns. For W7_01, the closest categories corresponded to regions associated with regulated and exploratory emission contexts, whereas categories associated with sustained negative contexts were among the most distant. In contrast, W8_03 exhibited greater proximity to high-activation categories, consistent with its denser textural and informational configuration. In both cases, the most distant categories were those characterized by contrasting acoustic organization rather than by superficial spectral similarity.

Crucially, proximity in the OAAS does not imply emotional identity. Instead, it indicates graded structural alignment between acoustic configurations. Such alignment is likely to contribute to affective processing—because vocalizations are shaped by the same perceptual constraints under which animals decode acoustic meaning—yet emotional significance remains context-dependent and cannot be inferred from geometry alone. OAAS therefore supports interpretation by combining geometric proximity with emission-context descriptors and, when available, external behavioral validation.

To resolve apparent overlap in two-dimensional OAAS projections and to quantify proximity more precisely, distances between program stimuli and vocalization-category centroids were computed across the full three-dimensional OAAS (PC1–PC3) and summarized at the level of program families (weeks). The resulting matrix reveals consistent patterns: across families, musical stimuli remain systematically closer to vocalization-derived centroids than to negative control noise, while preserving measurable separation from all reference categories. Importantly, proximity varies across families, indicating that convergence toward biologically grounded acoustic regions is selective rather than uniform.

This quantitative representation confirms that overlap in two-dimensional projections reflects graded proximity within a continuous acoustic–affective space, rather than categorical ambiguity or pointwise coincidence. The heatmap complements the geometric visualization in Figure 2 by explicitly resolving distances and directional relationships across the full three-dimensional OAAS.




![](Outputs/Figures_OAAS/Figure_4_OAAS_distance_heatmap_family_centroids_FINAL_300dpi.png){width=90%}



Figure 4. Acoustic–affective proximity between program music families and porcine vocalization-category centroids in the three-dimensional OAAS.
Heatmap showing Euclidean distances computed in the three-dimensional Operational Acoustic–Affective Space (OAAS; PC1–PC3) between family-level centroids of program musical stimuli (rows; W1–W10, program families) and centroids of porcine vocalization-derived reference categories (columns). Each cell reports the mean distance ± standard deviation across stimuli within each family. Lower distances indicate greater structural proximity within the OAAS, enabling quantitative comparison of acoustic–affective alignment between designed musical environments, vocalization-derived reference regions, and negative control sounds.

Complete distance rankings between musical stimuli and porcine vocalization categories are provided in Supplementary Table S1.

Together, OAAS projections, operability analyses, and distance-based comparisons demonstrate that the functional music program occupies biologically interpretable regions of the acoustic–affective space while preserving controlled separation from both natural vocal expression and unstructured noise. These findings support OAAS as a framework for evaluating and designing synthetic acoustic environments based on graded acoustic–affective relationships rather than categorical assumptions.

## 4. Discussion

The present study introduces the Operational Acoustic–Affective Space (OAAS) as an applied framework for the analysis, evaluation, and intentional design of affective sound environments. Conceptually, the article treats synthetic acoustic environments as affective systems as the applied domain, and positions OAAS as the primary methodological contribution: a reproducible coordinate space that makes such environments comparable, interpretable, and—within constraints—operable. Rather than reporting new behavioral or physiological experiments, the results examine how affect-relevant acoustic structure emerges and constrains design decisions when biologically grounded vocal reference signals, control noise, and designed sound environments are represented within a shared multidimensional space [@ISO12913_1_2014_Soundscape; @HerranzPascual2020_SoundscapeEmotionsReview; @FiebigEtAl2020_EmotionTheorySoundscape].

Across the case studies presented in Section 3, OAAS exhibited consistent structural behavior that supports its use as a design- and evaluation-oriented framework. Importantly, the contribution is not a new affect taxonomy nor a replacement for welfare-oriented classification approaches. Instead, it is a complementary representational strategy: OAAS formalizes a geometric domain in which heterogeneous sound environments can be positioned, compared, and intentionally displaced relative to biologically grounded reference regions, enabling reproducible reasoning about affect-oriented sound design [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals].

Despite substantial progress in soundscape research and affective approaches to environmental appraisal, the field still lacks a reproducible design geometry for intervention-oriented work. In practice, heterogeneous sound environments are rarely evaluated within a shared operational space that supports explicit geometric descriptors—such as centroids, distances, trajectories, and displacement—under standardized acoustic representations. This limits cross-study comparability and makes it difficult to formalize sound-based interventions as controllable affective systems with defined target regions and quantifiable directed change [@ISO12913_1_2014_Soundscape; @HerranzPascual2020_SoundscapeEmotionsReview]. OAAS is proposed to address this specific gap by enabling interpretable positioning and constrained navigation across biologically grounded reference regions and designed sound environments.

### 4.1. OAAS as a Framework for Affective Sound Environment Design and Evaluation

OAAS operationalizes synthetic acoustic environments as affective systems by treating time-extended sound environments as structured, measurable, and comparable configurations—rather than as isolated auditory exposures. Within this framing, synthetic acoustic environments are understood as intentionally constructed soundscapes designed to shape affective and regulatory conditions over time through integrated spectral, temporal, dynamic, and informational organization, consistent with soundscape conceptual frameworks and ecological approaches to acoustic environments [@ISO12913_1_2014_Soundscape; @PijanowskiEtAl2011_SoundscapeEcology; @FarinaGage2017_Ecoacoustics].

Recent interdisciplinary reviews have argued that progress in animal-centered music research is constrained by low reproducibility, heterogeneous protocols, and insufficient reporting of intrinsic stimulus properties and playback parameters [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. OAAS can be interpreted as an operational response to these priorities: by defining a standardized acoustic representation, explicit coordinate geometry, and biologically grounded anchoring, it enables reproducible positioning and quantitative comparison across heterogeneous sound environments. Moreover, OAAS-based design and verification workflows implicitly enforce systematic characterization of intrinsic acoustic properties and their transformation effects, aligning with ILPP-style reporting requirements while extending them into a navigable design space.

Rather than prescribing what these environments should sound like (music, noise, hybrid textures, or other forms), OAAS provides a unified basis for quantitative comparison and evaluation across sound sources. This supports reproducible interpretation of intervention structure and enables operational analyses based on geometric relationships (e.g., centroids, distances, and displacement), linking acoustic characterization directly to design-oriented reasoning under real-world constraints [@Farina2021_EcoFieldTheory; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. This framing also clarifies why OAAS can incorporate biological anchoring without reducing affect to categories: affective plausibility is approached through graded structural alignment in a shared coordinate space rather than categorical assignment [@BrieferEtAl2022_SciRepSoundWel; @ZapataCardona2024_AnimalsReview].

### 4.2. Biologically Grounded Anchoring without Category Reduction (revised)

Using porcine vocalizations as an anchoring reference grounds OAAS in natural sound production rather than in purely conceptual affect labels. Importantly, this anchoring does not imply that the framework “re-validates” SoundWel or seeks to outperform its approach. Instead, SoundWel functions as a biologically grounded substrate that populates OAAS with reference regions derived from well-defined emission contexts and valence-related descriptors, enabling interpretability without imposing categorical affect structure on the space [@BrieferEtAl2022_SciRepSoundWel; @Briefer2012_VocalExpressionEmotionsMammals; @LaurijsBrieferReimertWebb2021_FarmAnimalVocalisationsPositiveWelfare].

This distinction matters because classification-oriented approaches and OAAS address different questions. Classification strategies are designed for context-aware recognition and welfare-oriented monitoring of vocal outputs, often emphasizing predictive performance and robustness under field conditions [@BrieferEtAl2022_SciRepSoundWel; @CoutantVillainBriefer2024_BioacousticsWelfareReview; @XieEtAl2024_ASTAbnormalPigVocalizations]. Recent work also highlights that robustness across farms remains limited by environmental variability and behavioral diversity, reinforcing that classification accuracy alone does not resolve the representational problem of comparability across heterogeneous acoustic contexts [@VandetPannEtAl2026_RobustPigVocalizationCNN]. OAAS complements these perspectives by offering an operational geometric representation: rather than predicting categories, OAAS enables comparison and design by quantifying proximity, separation, and displacement between heterogeneous sound environments and vocalization-derived reference regions under standardized acoustic representations [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals].

A related methodological point concerns the role of QBA alignment. If OAAS dimensions are operational rather than categorical, why align vocal emission contexts with QBA-informed descriptors at all? The purpose is interpretability and methodological continuity—not categorical equivalence. In animal-centered sound research, affect must be inferred from objective indicators and contextual evidence. QBA provides a validated observer-based bridge between acoustic environments and organismal state in intervention contexts [@ZapataCardona2022_SciRepGrowingPigs; @ZapataCardona2023_SciRepSpectroTemporal]. Vocal emission contexts, in turn, provide biologically grounded reference signals. Their conceptual alignment supports coherent interpretation across datasets and methods without implying that acoustic proximity alone determines emotional identity [@ZapataCardona2024_SciRepMusicProgram].

Crucially, OAAS proximity should be interpreted as graded structural alignment. It does not guarantee identical emotional experience across sound sources; however, it is expected to contribute to affective plausibility because vocalizations and designed environments are constrained by the same perceptual system and by ecologically relevant acoustic regularities [@ZapataCardona2024_AnimalsReview]. Notably, comparative neurophysiological evidence indicates that mammalian brains exhibit both general and conspecific sensitivity to vocal sounds, suggesting that vocalizations occupy privileged perceptual status and provide biologically meaningful anchors for acoustic modeling [@MorvaiEtAl2025_EEGVocalizationSensitivity]. Accordingly, OAAS interpretation is strongest when geometry is read together with emission-context descriptors and, where available, external behavioral or physiological validation, rather than treated as a stand-alone affect inference mechanism [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @BrieferEtAl2022_SciRepSoundWel].

Importantly, OAAS is an acoustic–geometric representational space, not an affective state space. Unlike valence–arousal models used in psychology—where coordinates are defined as subjective or behavioral affect ratings—OAAS coordinates are defined by quantitative acoustic descriptors and reference anchoring using biologically grounded signals. Therefore, OAAS does not “locate emotions” in a psychological sense; rather, it locates sound environments in a reproducible feature geometry, enabling structural comparison and constrained navigation across reference regions. Any affective interpretation must be made through the joint reading of OAAS geometry, emission-context descriptors, and independent behavioral or physiological validation evidence. This distinction is consistent with soundscape frameworks in which perception and appraisal depend on listener, context, and environmental conditions, and where acoustic descriptors are necessary but not sufficient predictors of affective outcomes [@ISO12913_1_2014_Soundscape; @FiebigEtAl2020_EmotionTheorySoundscape; @KriengwatanaMottTenCate2022_MusicAnimalWelfare]. OAAS thereby supports interpretability while preserving conceptual openness regarding affective inference and welfare relevance [@KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals].

### 4.3. From Music to Functional Sound Environments

A persistent challenge in animal-centered sound research is the conceptual and terminological ambiguity between “music,” “soundscape,” and broader categories of synthetic acoustic environments. Recent interdisciplinary reviews explicitly note that the field still lacks an operational definition of “music” in non-human contexts and, as a consequence, struggles to establish reproducible standards for stimulus design and evaluation [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. OAAS contributes to resolving this issue by treating music as one possible implementation of an affective sound environment, rather than as a privileged or conceptually protected category.

In the present framework, music is understood as an intentional soundscape: a constructed acoustic micro-ecosystem in which spectral, temporal, dynamic, and spatial relations interact over time to generate coherent perceptual and affective contexts. This position aligns with foundational acoustic ecology perspectives in which music can be interpreted as an intentional reorganization of the soundscape and of communicative sound patterns [@Schafer1977_TheSoundscape; @Truax2001_AcousticCommunication]. Within OAAS, the relevant distinction is therefore not whether a stimulus is “music” in a cultural sense, but whether its acoustic organization functions as a coherent affective system aligned with regulatory objectives, and how that organization maps onto biologically grounded reference regions.

This operational framing also addresses a practical limitation highlighted in the literature: animal music studies frequently rely on pre-existing human repertoires, selected without systematic control of acoustic structure, species-perceptual accessibility, or functional objectives. In response to that gap, our previous work introduced the concept of veterinary functional music: music composed or selected for a defined welfare-related function, empirically validated in a target species, and engineered through acoustic and musical adjustments suitable for the sensory and perceptual characteristics of that organism [@ZapataCardona2022_SciRepGrowingPigs; @ZapataCardona2024_SciRepMusicProgram; @AlvarezHernandez2023_AnimalsEnrichment]. This concept prioritizes function, validation, and acoustic design over cultural origin or human aesthetic convention.

Importantly, OAAS extends this functional approach into a reproducible design and evaluation geometry. By positioning both vocalizations and constructed sound environments within a shared acoustic–affective coordinate space, OAAS enables functional music—and other engineered sound environments—to be analyzed and calibrated as systems with measurable trajectories, distances, and constrained transformations. In this sense, OAAS provides a methodological bridge between compositional intention, production-level engineering, and quantitative verification, supporting the reproducible development of affective sound environments suitable for enrichment, interspecies-compatible shared soundscapes, or aversive acoustic configurations when the objective is deterrence or risk avoidance [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals].

Finally, this perspective is particularly important in animal-centered work because auditory perception is adapted to ecological contexts and to the acoustic structure of environments in which vocalizations naturally occur. Vocalizations therefore serve here not as templates for “species-specific music,” but as ecologically grounded anchors reflecting affect-relevant communication under real-world constraints [@BrieferEtAl2022_SciRepSoundWel; @Briefer2012_VocalExpressionEmotionsMammals]. Accordingly, OAAS supports a conceptual shift away from categorical assumptions about “species-specific music” and toward an operational view of sound as an engineered ecological medium whose organization can be designed to support regulation, engagement, resilience, or avoidance depending on context and objective.

### 4.4. Noise, Roughness, Entropy, and the Limits of Broadband Controls 

A notable outcome concerns the relationship between broadband noise and affective interpretation. Although noise-based controls are often recommended in animal-centered sound research—partly because they may mask environmental noise and reduce confounds when comparing musical stimuli across settings [@KriengwatanaMottTenCate2022_MusicAnimalWelfare]—our OAAS analyses suggest that noise should not be treated as a purely neutral control condition. Instead, broadband noise may function as an active acoustic stimulus with its own perceptual and regulatory effects.

Evidence from human studies supports this interpretation: white noise has been associated with increased heart rate variability (HRV) during short listening exposures, and stochastic noise embedded into slow-tempo music may enhance autonomic coherence through mechanisms consistent with stochastic resonance [@PepplinkhuizenEtAl2026_WhiteNoiseHRV; @DiazLozanoEtAl2026_NoiseHRVCoherence]. Together, these findings motivate treating broadband noise not only as a masking baseline, but as a potentially functional acoustic intervention.

In our lactation study, pink noise and veterinary functional music were evaluated as separate treatments relative to a no-stimulation control condition, and both interventions showed favorable effects on maternal behavior and piglet outcomes [@MontoyaZuluaga2025_SciRepSowsInPress]. These results reinforce the idea that noise-based stimulation can produce measurable functional effects independent of any masking role, and should therefore be treated as an experimental condition rather than as a trivial baseline.

Porcine vocalizations—particularly in high-activation contexts—often contain noise-like components, high spectral density, and irregular temporal structure. However, such “noisy” biological signals are not equivalent to unstructured broadband noise. Vocalizations exhibit informational organization shaped by production constraints and communicative function, including non-random temporal patterning and structured variability across call types and emission contexts [@BrieferEtAl2022_SciRepSoundWel]. In this sense, affect-relevant roughness emerges not merely from spectral density, but from structured irregularity.

Such irregularity can be operationalized through entropy-related descriptors (e.g., temporal entropy, spectral entropy, multiscale entropy, dispersion profiles). This interpretation aligns with growing evidence that multiple acoustic parameters jointly encode robust communicative contrasts across contexts in mammalian-directed vocal communication [@GABOR2026106284]. OAAS captures this distinction by integrating descriptors that reflect both spectral texture and informational structure, enabling unstructured broadband noise to be differentiated from biologically grounded irregularity.

From an applied perspective, this implies that noise-based sound environments should not be evaluated solely by spectral profile; their temporal and informational organization is critical for interpreting likely perceptual impact and for assessing proximity to vocalization-derived reference regions. The present study did not systematically differentiate between broadband profiles (e.g., white vs. pink vs. brown), which remains a limitation and an opportunity for future work. OAAS provides a suitable framework for examining how different broadband structures—and their entropy-related signatures—populate the acoustic–affective space and how they might be used (or avoided) in functional affective sound environment design.

### 4.5. Post-Hoc Evaluation: Functional Organization over Stylistic Identity 

OAAS-based post-hoc evaluation showed that stimuli sharing compositional and production strategies converge within the acoustic–affective space despite differences in musical surface features. This indicates that OAAS captures functional acoustic organization rather than stylistic identity, which is particularly relevant in applied settings where sound environments may be implemented as music, hybrid textures, or engineered noise-like structures, yet remain comparable in terms of their spectral–temporal and informational organization.

Stimuli positioned near vocalization-derived regions linked to high activation should not be interpreted as inherently aversive. Instead, proximity reflects shared structural properties such as spectral density, temporal irregularity, and informational load, which can occur both in affect-relevant vocal communication and in designed environments that increase acoustic complexity. This distinction motivates a core interpretive rule of OAAS: geometric proximity does not imply identity of emotional experience. Rather, it indicates graded structural alignment within a shared coordinate system, which can inform design decisions and post-hoc interpretation—particularly when read alongside emission-context descriptors, listener constraints, and external validation evidence.

This interpretive stance is aligned with soundscape and affective appraisal approaches, in which acoustic features contribute to affective plausibility but do not fully determine perceived emotion or welfare outcomes. Such outcomes remain context-dependent and mediated by listener characteristics and playback conditions [@ISO12913_1_2014_Soundscape; @FiebigEtAl2020_EmotionTheorySoundscape]. Accordingly, OAAS functions as a representational geometry for sound environments, enabling reproducible structural comparison while preserving conceptual openness regarding affective interpretation [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals].

### 4.6. Operability and Constraints: OAAS as a Constrained Control Space 

The directed displacement experiments demonstrate that OAAS is not merely descriptive but operable. Controlled transformations enabled intentional navigation toward predefined reference regions, quantified geometrically. Positive-directed displacement was consistently achievable across stimuli, whereas negative-directed displacement exhibited stimulus-dependent constraints and saturation effects when stimuli were already positioned near negative reference regions.

These constraints are informative rather than limiting. They characterize feasible transformation regions and boundary conditions for affect-oriented design, reinforcing OAAS as a constrained design space rather than an unconstrained generative mechanism. In applied work, such constraints are valuable because they define what is realistically achievable while preserving coherence and acceptable parameter ranges.

To our knowledge, comparable displacement-based control spaces have not been explicitly formalized in animal-centered affective sound environment design. Therefore, we interpret these findings as an operational contribution rather than a direct replication of an established methodological precedent. Importantly, this novelty also requires disciplined hypothesis framing: OAAS does not claim universal controllability of affective outcomes, but rather defines a falsifiable space of constrained transformations whose validity must be evaluated under explicit assumptions and context-dependent limits [@Pulina2025_SoundUseExperimentalHypotheses].

Related methodological analogies exist in applied acoustics and engineering domains, where robust performance under real-world noise and reverberation conditions is achieved by combining compact latent representations with lightweight, interpretable filtering mechanisms. Such approaches emphasize the practical value of constraint-aware latent control spaces, especially when deployment conditions impose strong boundary limits [@GuiEtAl2025_LatentDeepKernelFiltering].

In this sense, OAAS operability should be interpreted as constrained navigability: the ability to produce measurable displacement within a feature geometry while respecting acoustic plausibility, listener constraints, and parameter coherence. The observed saturation effects therefore function as empirical indicators of the feasible transformation manifold, supporting OAAS as a structured control space for functional affective sound environment design rather than as an unconstrained generative system.

### 4.7. Texture-Level Modulation with Structural Preservation 

Across transformations, OAAS-guided modifications preserved higher-level musical organization while modulating fine-grained acoustic texture (spectral redistribution, granularity, and temporal micro-structure). This supports an applied principle: affect-oriented sound environment design does not necessarily require reauthoring musical content, but can be approached through controlled modulation of acoustic materiality while maintaining structural coherence.

Importantly, recent farm-based evidence indicates that both functional music and pink noise can yield favorable outcomes relative to non-stimulated controls in lactating sows, reinforcing that intervention effects must be interpreted relative to the baseline farm soundscape rather than against an implicit “silence” condition [@MontoyaZuluaga2025_SciRepSowsInPress]. OAAS provides a framework to quantify such baseline-to-intervention shifts and to compare distinct intervention strategies within a shared coordinate space.

A key implication is that the functional positioning of a sound environment may depend critically on production-level processes, even when the underlying musical composition remains unchanged. The same piece can occupy different OAAS regions depending on timbral balance, spectral density, loudness structure, and micro-dynamic organization introduced during synthesis, mixing, and post-production [@ZapataCardona2023_SciRepSpectroTemporal; @ZapataCardona2024_AnimalsReview]. This has methodological relevance for animal-centered sound research, where stimuli are often drawn from existing human repertoires without systematic control of acoustic structure or perceptual accessibility, potentially introducing uncontrolled variance in affective outcomes [@KriengwatanaMottTenCate2022_MusicAnimalWelfare].

From an applied welfare and health perspective, this suggests that sound-based interventions require quality-control procedures analogous to those used in other biological treatments, where dosage, formulation, and reproducibility are essential. In this sense, OAAS provides a calibration tool capable of verifying and adjusting production-sensitive configurations, enabling sound environments to be treated as operational affective systems rather than static musical artifacts [@KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals; @ZapataCardona2024_SciRepMusicProgram].

This aligns with the broader operational framing of synthetic acoustic environments as affective systems: the objective is not to produce a categorical type of sound, but to shape how organized acoustic structure supports regulation, engagement, and affective plausibility under ecological constraints [@ISO12913_1_2014_Soundscape; @FiebigEtAl2020_EmotionTheorySoundscape].

### 4.8. Datasets as Research Infrastructure and Framework Generalization

The present work also highlights the broader significance of shared audio datasets—such as vocalization corpora and environmental recordings—as research infrastructure. Such datasets enable multiple methodological approaches to coexist: welfare-oriented classification and monitoring, mechanistic feature-based analysis, and design-oriented synthesis. OAAS is intended as a framework that leverages these resources to support design and evaluation workflows in a transparent, reproducible way.

In the specific case of the porcine anchoring model, the SoundWel project provides a labeled reference corpus of pig calls produced in clearly defined contexts and organized along valence-related descriptors. The availability of this dataset as a public, versioned research resource—together with its associated methodological framework—supports OAAS interpretability and reproducibility by enabling reference regions to be grounded in biologically meaningful emissions rather than abstract affect labels [@BrieferEtAl2022_SciRepSoundWel; @BrieferEtAl2022_SoundwelDataset_Zenodo].

Although this study uses porcine vocalizations as a reference model, OAAS is not species-specific in scope. The porcine model provides a controlled test case for evaluating how the framework behaves under realistic acoustic and affective constraints. The methodological logic underlying OAAS is transferable and can be extended to other species and applied domains where objective measures of sound structure and response indicators are available.

From a methodological perspective, the combination of open datasets and standardized acoustic representations offers a pathway toward cumulative and comparable research. As animal-centered sound interventions expand beyond exploratory demonstrations, shared repositories become critical for benchmarking, replication, and cross-context generalization. In this sense, OAAS can be understood as a design-oriented complement to dataset-driven monitoring approaches: it offers a geometric infrastructure that enables heterogeneous stimuli (music, noise, environmental recordings, vocalizations) to be compared and calibrated within a common operational space.

More broadly, this dataset-centered paradigm supports framework generalization: as additional corpora become available—across species, contexts, and recording conditions—OAAS can incorporate new anchoring regions and expand its representational coverage. This suggests a future research infrastructure in which vocalization datasets and soundscape repositories function not only as monitoring resources but also as calibration layers for functional affective sound environment design.

4.9. Limitations and Future Directions

An important limitation of the present work is that OAAS is demonstrated primarily as an acoustic–affective design and evaluation geometry, without introducing new behavioral or physiological experiments. Although OAAS supports reproducible positioning and directed acoustic transformations, its interpretive strength ultimately depends on well-documented listener and playback conditions. Recent interdisciplinary proposals emphasize that intrinsic stimulus properties, listener characteristics, playback context, and producer-related assumptions (ILPP) are frequently underreported in animal sound and music research, limiting reproducibility and mechanistic interpretation [@KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. This concern is consistent with broader conceptual critiques highlighting the need for explicit operational definitions and standardized reporting to enable cumulative progress across studies [@KriengwatanaMottTenCate2022_MusicAnimalWelfare].

Future work should therefore integrate OAAS with ILPP-style reporting standards and robust experimental framing, including systematic playback calibration (e.g., SPL, background soundscape, speaker configuration), listener history and sensory constraints, and production-level parameter reporting. Such integration would enable OAAS-based outcomes to be compared across studies and species within a shared reproducible framework, while preserving the interpretive distinction between acoustic geometry and affective inference. In this sense, OAAS is best understood as a falsifiable operational space whose predictions remain conditional on explicit assumptions and documented constraints, consistent with recent calls for disciplined hypothesis structure in animal science [@Pulina2025_SoundUseExperimentalHypotheses].

The present study is additionally limited to acoustic analysis and expert structural inspection; no claims are made regarding generalized perceptual equivalence across listeners or direct behavioral effects within the present dataset. Future research should extend OAAS through: (i) adaptive or closed-loop control strategies, (ii) systematic comparisons of broadband sound structures (e.g., pink, brown, and filtered noise profiles), and (iii) species-appropriate auditory weighting models. Moreover, OAAS-based design principles should be evaluated through multimodal validation combining acoustic, behavioral, and physiological indicators, particularly in ecological farm contexts where baseline soundscapes and variability strongly influence intervention outcomes [@MontoyaZuluaga2025_SciRepSowsInPress]. These extensions are expected to strengthen OAAS as a translational tool for evidence-based design of welfare-oriented and restorative sound environments across animal and human contexts [@ZapataCardona2024_AnimalsReview].

Finally, the broader trajectory suggested by OAAS supports treating affective sound environments as operational systems rather than static artifacts. Evidence from clinical and built-environment domains indicates that both music and structured non-musical sound interventions can modulate physiological and psychological outcomes (e.g., sleep, stress biomarkers, perceived relaxation), reinforcing the relevance of calibrated acoustic design beyond traditional “music” paradigms [@PapathanassoglouEtAl2025_ICUSoundMusicReview; @ZhangEtAl2025_EEG_AcousticEnvironment]. Controlled studies further show that sound-based environmental design can influence behavior and social interaction without adverse emotional effects, supporting the practical value of constraint-aware sound design frameworks in real-world settings [@SunEtAl2025_BackgroundSoundOffice; @SuEtAl2026_SoundDesignChildrenInteraction]. Together, these directions define a scalable research agenda for OAAS validation and deployment across species and shared human–animal environments.

## 5. Conclusions

Animal-centered sound and music research continues to face persistent methodological limitations, including heterogeneous experimental designs and insufficient reporting of stimulus properties and playback context [@KriengwatanaMottTenCate2022_MusicAnimalWelfare; @KriengwatanaNagerSouthUllrichDoolittle2025_PlayingMusicToAnimals]. To address these constraints, the present study introduces the Operational Acoustic–Affective Space (OAAS) as an applied coordinate framework enabling quantitative comparability and constraint-aware navigation across heterogeneous sound environments using biologically grounded anchoring.

OAAS builds on a cumulative empirical trajectory from our group, including: (i) a comparative synthesis of music and emotions in non-human animals [@ZapataCardona2024_AnimalsReview]; (ii) evidence that pigs exposed to original musical constructions exhibit differentiated emotional responses quantified through QBA [@ZapataCardona2022_SciRepGrowingPigs]; (iii) mechanistic links between these responses and engineered spectro-temporal configurations [@ZapataCardona2023_SciRepSpectroTemporal]; (iv) applied evidence that adapted original music can reduce aggression during regrouping [@AlvarezHernandez2023_AnimalsEnrichment]; (v) validation of a long-duration functional music program with measurable psychophysiological effects related to chronic stress [@ZapataCardona2024_SciRepMusicProgram]; and (vi) farm-based lactation evidence showing favorable effects on maternal behavior and reduced pre-weaning piglet mortality [@MontoyaZuluaga2025_SciRepSowsInPress]. Together, these studies support OAAS as a translational strategy integrating art- and engineering-driven stimulus design with behavioral, emotional, and physiological evaluation.

By integrating biologically grounded reference signals, quantitative acoustic descriptors, and controlled transformation strategies within a unified multidimensional space, OAAS supports both post-hoc evaluation and design-oriented calibration through measurable distances, trajectories, and constrained transformations. Across the presented cases, OAAS demonstrated three complementary capabilities: (i) construction of a biologically grounded acoustic–affective reference space using natural vocal expression; (ii) evaluation of designed sound environments based on functional acoustic organization rather than stylistic identity; and (iii) operability as a constrained control space supporting directed displacement toward predefined reference regions while preserving structural coherence. Importantly, navigation was not uniformly bidirectional: region-specific constraints and saturation effects emerged as intrinsic properties of the geometry, delineating feasible transformation boundaries for affect-oriented design.

Although porcine vocalizations served here as the biologically grounded anchoring model, OAAS is not species-specific in conceptual scope. Rather, it provides a transferable operational logic for any domain in which objective measures of sound structure and response indicators are available, supporting cumulative progress toward reproducible science and evidence-based design of welfare-oriented and restorative sound environments across animal and human contexts.

Finally, OAAS is proposed as a foundational and extensible research infrastructure. The authors invite other researchers to apply, test, benchmark, and improve OAAS across species, datasets, and ecological contexts, contributing additional reference signals, descriptors, and validation protocols. In this way, OAAS aims to support a reproducible and goal-oriented science of affective sound environments, bridging biological anchoring, engineering control, and translational design.

**Author Contributions:**
Conceptualization, J.Z.-C. and B.d.J.R.; writing—original draft preparation, J.Z.-C.; writing—review and editing, J.Z.-C., B.d.J.R. and M.C.C.; supervision, B.d.J.R. and M.C.C.; project administration, B.d.J.R.; funding acquisition, B.d.J.R. All authors have read and agreed to the published version of the manuscript.

**Funding:**
This research was jointly supported by the Ministerio de Ciencia, Tecnología e Innovación (Minciencias) under Convocatoria 890 – Strengthening Science, Technology and Innovation in Higher Education Institutions (contract ICETEX 2021–1091) and by the Programmatic Call 2020 – Social Sciences, Humanities and Arts of Universidad de Antioquia (Medellín, Colombia).

**Institutional Review Board Statement:**
Not applicable.

**Informed Consent Statement:**
Not applicable.

**Supplementary Materials:** The following supporting information can be downloaded from the submission system and/or the associated repository: Supplementary Table S1: OAAS distances between music-derived environments and control categories; Supplementary Table S2: explained variance and cumulative variance for the 3D PCA OAAS solution; Supplementary Table S3: PCA loadings (PC1–PC3) for OAAS variables.

**Data Availability Statement:** 
The minimal reproducible datasets (CSV) required to reproduce Supplementary Tables S1–S3, the scripts used for reproducibility, and the Figure 3 audio examples (excluding proprietary SoundWel audio) are available in the public GitHub repository oaas-applied-sciences-supplementary, release v1.0.0: https://github.com/berardorodriguez/oaas-applied-sciences-supplementary/releases/tag/v1.0.0odo record.

**Acknowledgments:** 
We thank John P. Kastelic (University of Calgary) for his unconditional support in correcting style and English grammar.

**Conflicts of Interest:**
The authors declare no conflicts of interest.

## References




