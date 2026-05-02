import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="The Journey of the Be Like Brit Kids – built by Gesner Deslandes",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LANGUAGE STATE ----------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- UI TRANSLATIONS ----------
ui_text = {
    "en": {
        "app_title": "📘 The Journey of the Be Like Brit Kids",
        "app_sub": "Inspiring stories of hope, resilience, and love from Haiti – built by Gesner Deslandes",
        "app_authors": "Authored by: Daya JOACHIM, Guerlanda PIERRE LOUIS, Djoudemie JEAN BAPTISTE, Sandiana SEPTEMBRE",
        "sidebar_website": "🌍 Visit Be Like Brit",
        "sidebar_book_title": "📖 The Journey of the Be Like Brit Kids",
        "sidebar_book_desc": "Inspiring stories of hope, resilience, and love from Haiti",
        "sidebar_caption": "Built by Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Select Chapter",
        "read_aloud_button": "🔊 Read Aloud",
        "reading_indicator": "🔊 Now reading... (audio playing)",
        "reading_success": "🔊 Now reading aloud... (make sure your device volume is on)",
        "footer_copyright": "GlobalInternet.py – Storytelling by Gesner Deslandes",
        "footer_book": "📖 \"The Journey of the Be Like Brit Kids\" – A book of hope from Haiti",
        "footer_built": "🌐 Built with Streamlit | Hosted on GitHub + Streamlit Cloud",
        "language_selector": "🌐 Language",
    },
    "fr": {
        "app_title": "📘 Le Voyage des Enfants de Be Like Brit",
        "app_sub": "Histoires inspirantes d'espoir, de résilience et d'amour d'Haïti – construit par Gesner Deslandes",
        "app_authors": "Auteurs : Daya JOACHIM, Guerlanda PIERRE LOUIS, Djoudemie JEAN BAPTISTE, Sandiana SEPTEMBRE",
        "sidebar_website": "🌍 Visitez Be Like Brit",
        "sidebar_book_title": "📖 Le Voyage des Enfants de Be Like Brit",
        "sidebar_book_desc": "Histoires inspirantes d'espoir, de résilience et d'amour d'Haïti",
        "sidebar_caption": "Construit par Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Choisir le chapitre",
        "read_aloud_button": "🔊 Lire à voix haute",
        "reading_indicator": "🔊 Lecture en cours... (audio en cours)",
        "reading_success": "🔊 Lecture en cours... (vérifiez le volume de votre appareil)",
        "footer_copyright": "GlobalInternet.py – Contes par Gesner Deslandes",
        "footer_book": "📖 \"Le Voyage des Enfants de Be Like Brit\" – Un livre d'espoir d'Haïti",
        "footer_built": "🌐 Construit avec Streamlit | Hébergé sur GitHub + Streamlit Cloud",
        "language_selector": "🌐 Langue",
    },
    "es": {
        "app_title": "📘 El Viaje de los Niños de Be Like Brit",
        "app_sub": "Historias inspiradoras de esperanza, resiliencia y amor desde Haití – construido por Gesner Deslandes",
        "app_authors": "Autores: Daya JOACHIM, Guerlanda PIERRE LOUIS, Djoudemie JEAN BAPTISTE, Sandiana SEPTEMBRE",
        "sidebar_website": "🌍 Visite Be Like Brit",
        "sidebar_book_title": "📖 El Viaje de los Niños de Be Like Brit",
        "sidebar_book_desc": "Historias inspiradoras de esperanza, resiliencia y amor desde Haití",
        "sidebar_caption": "Construido por Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Seleccionar capítulo",
        "read_aloud_button": "🔊 Leer en voz alta",
        "reading_indicator": "🔊 Leyendo ahora... (audio en curso)",
        "reading_success": "🔊 Leyendo en voz alta... (asegúrese de que el volumen de su dispositivo esté activado)",
        "footer_copyright": "GlobalInternet.py – Narración por Gesner Deslandes",
        "footer_book": "📖 \"El Viaje de los Niños de Be Like Brit\" – Un libro de esperanza desde Haití",
        "footer_built": "🌐 Construido con Streamlit | Alojado en GitHub + Streamlit Cloud",
        "language_selector": "🌐 Idioma",
    }
}

def _(key):
    return ui_text[st.session_state.lang].get(key, key)

# ---------- CHAPTERS: ENGLISH ----------
chapters_en = [
    {
        "title": "Be Like Brit Location on the mountain top in Grand Goave national road # 2",
        "image": "https://raw.githubusercontent.com/Deslandes1/The-Journey-of-the-Be-Like-Brit-Kids/main/home.jpg",
        "text": "Britney Gengel was a young American woman who fell in love with Haiti and its children. During a mission trip in January 2010, she called her parents from her cell phone just before the devastating earthquake struck. With tears in her voice, she said, 'I love you, and I want to come back here and build an orphanage for these beautiful kids.' Minutes later, the earth shook. Britney lost her life in the rubble, but her dream did not die. Her parents, Len and Cherylann Gengel, decided to make her wish come true. They founded the Be Like Brit Foundation and built a safe, earthquake‑resistant orphanage on a mountaintop in Grand‑Goâve, overlooking National Road #2. The building is shaped like a 'B' – for Brit. Today, dozens of children live, learn, and play there, surrounded by love and opportunity. This is the story of a girl who dreamed of giving a home, and of a community that made that dream a reality.",
        "caption": "The Be Like Brit orphanage seen from above – a 'B' shape on the mountain"
    },
    {
        "title": "Chapter 2: The First Day of School",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&auto=format",
        "text": "The bell rang at 7:30 AM. Jean‑Pierre, age nine, had never been to school before. He held his new backpack tightly, a gift from the house parents. The classroom was simple – wooden desks, a chalkboard, and a map of Haiti on the wall. His teacher, Madame Claire, smiled at him. 'Bonjour, Jean‑Pierre. Today, you will learn to write your name.' He was nervous, but the other children shared their crayons with him. By the end of the day, he could write 'Jean‑Pierre' in big blue letters. He ran to show the other kids. 'Look what I did!' he shouted. That night, he vowed to become an engineer one day. He wanted to build schools for other children like him. His journey had started with a single letter.",
        "caption": "Children learning in a bright classroom"
    },
    {
        "title": "Chapter 3: The Garden of Hope",
        "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=600&auto=format",
        "text": "Behind the orphanage, there was a small garden. It was overgrown with weeds, but the children saw potential. Led by their mentor, Jonas, they decided to turn it into a vegetable garden. 'We will grow our own food,' he said. Every afternoon, they dug the soil, planted seeds, and watered the young plants. The first week was hard; their hands got dirty and their backs ached. But they worked together. Rose, a twelve‑year‑old girl, loved watching the tiny sprouts appear. 'They look like little soldiers fighting their way to the sun,' she said. Two months later, they harvested tomatoes, carrots, and beans. The cook used them to make a delicious stew. Everyone ate together, proud of what they had grown. The garden became a symbol of their strength: even in hard soil, beautiful things can bloom.",
        "caption": "Children working together in a garden"
    },
    {
        "title": "Chapter 4: A Letter from Afar",
        "image": "https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=600&auto=format",
        "text": "One day, a letter arrived at the orphanage. It was from a college student in Boston who had heard about Be Like Brit. Her name was Sarah, and she wanted to become a pen pal to one of the kids. The director chose Elie, a quiet 14‑year‑old boy who loved drawing. Elie wrote his first letter in careful French: 'My name is Elie. I like to draw birds. What is your favourite animal?' Weeks passed, and a reply came. Sarah sent pictures of the Boston skyline and a drawing of a parrot. Elie was overjoyed. He started drawing every day, planning to become an artist. Their letters went back and forth for years. Elie’s art improved, and he learned English from Sarah’s notes. One day, he said, 'A friend across the ocean believed in me. Now I believe in myself.'",
        "caption": "A child writing a letter by lamplight"
    },
    {
        "title": "Chapter 5: The Big Match",
        "image": "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=600&auto=format",
        "text": "Soccer was the heartbeat of the orphanage. Every Saturday, the older kids challenged the younger ones to a friendly match. This time, the prize was a shiny new trophy donated by a visitor. The older team was confident – they had height and experience. But the younger team had speed and hunger. The match was intense. With five minutes left, the score was 2–2. Little Joseph, only ten years old, received a pass near the goal. He closed his eyes and kicked. The ball flew straight into the net. The younger team erupted in cheers. Joseph was carried on their shoulders. That night, the trophy was placed in the common room. Joseph said, 'We proved that size doesn’t matter. What matters is the size of your heart.' The older team shook hands and smiled. Everyone was a winner that day.",
        "caption": "Children playing soccer in a field"
    },
    {
        "title": "Chapter 6: The Art of Giving",
        "image": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=600&auto=format",
        "text": "Christmas was approaching, and the children were excited. But instead of asking for gifts, they decided to give. They made handmade cards and bracelets. They practiced songs in the church choir. On Christmas Eve, they visited a nearby nursing home. The elderly residents had no families left. The children sang carols, handed out their crafts, and sat with the old people. An old man named Pierre cried tears of joy. 'I have not been visited in years,' he said. 'You are angels.' The children returned home with full hearts. That year, they learned that giving is a gift in itself. One child, Mirlande, said, 'We have so little, but we can still share. That is the true magic of Christmas.'",
        "caption": "Children sharing gifts with elderly people"
    },
    {
        "title": "Chapter 7: The Storm",
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=600&auto=format",
        "text": "A hurricane was approaching. The sky turned dark, and the wind howled. The children were scared. The house parents gathered them in the main hall. They lit candles and told stories to keep everyone calm. For two days, the rain poured, and the wind shook the walls. But the building held strong, thanks to the engineers who had built it. When the storm passed, the children saw that the garden was destroyed and some trees had fallen. But they were all alive. They worked together to clean up. They planted new seeds in the garden. 'Storms will come,' said Jonas, 'but we are stronger than any storm.' The children understood that home is not just walls; it is the people inside them.",
        "caption": "A hurricane seen through a window"
    },
    {
        "title": "Chapter 8: The Visitor",
        "image": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=600&auto=format",
        "text": "One afternoon, a car pulled up to the gate. A tall man in a suit stepped out. He was a filmmaker from the United States. He had heard about Be Like Brit and wanted to make a documentary. The children were shy at first, but soon they opened up. They showed him their art, their soccer field, their garden. He filmed them laughing, studying, and helping each other. When the documentary was released, people around the world saw the children's courage. Donations poured in. A new dormitory was built. The children learned that their story had power. 'We are not just victims,' said one of the older boys, 'we are heroes of our own lives.' The filmmaker stayed in touch and visited every year.",
        "caption": "A filmmaker interviewing a child"
    },
    {
        "title": "Chapter 9: Graduation Day",
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&auto=format",
        "text": "Marie, now 18, had finished school. She stood on a small stage in the courtyard, wearing a white dress. All the children, staff, and some neighbours had gathered. The house mother handed her a certificate. Marie gave a speech. 'When I came here, I could not even speak. I was afraid of everything. But you gave me a family. You gave me an education. You gave me hope.' She planned to study nursing at a university. She would be the first in her cohort to go to college. The younger children cheered for her. They saw that one day, they too could walk across that stage. Marie hugged each of them. 'I will come back,' she promised. 'I will help those who come after me.' Her journey was just beginning, but she had already travelled so far.",
        "caption": "A proud graduate holding a certificate"
    },
    {
        "title": "Chapter 10: A Bright Future",
        "image": "https://images.unsplash.com/photo-1509099836639-18b84c05e2cb?w=600&auto=format",
        "text": "Today, the children of Be Like Brit are doctors, nurses, teachers, artists, and engineers. They live in Haiti and abroad, but they never forget where they came from. Every year, on the anniversary of the orphanage, many return. They play soccer with the new kids, share meals, and tell stories of their own journeys. The garden still grows vegetables. The classroom still resounds with lessons. The walls still stand strong, like the love that built them. The journey of the Be Like Brit kids is not just about survival. It is about thriving. It is about taking a small seed of hope and nurturing it until it becomes a tree that shades many. And the story continues, with every new child who walks through the gate.",
        "caption": "Children raising their hands in hope"
    }
]

# ---------- CHAPTERS: FRENCH ----------
chapters_fr = [
    {
        "title": "Emplacement de Be Like Brit sur la montagne à Grand‑Goâve route nationale #2",
        "image": chapters_en[0]["image"],
        "text": "Britney Gengel était une jeune Américaine qui est tombée amoureuse d'Haïti et de ses enfants. Lors d'un voyage missionnaire en janvier 2010, elle a appelé ses parents sur son téléphone portable juste avant que le violent tremblement de terre ne frappe. La voix chargée d'émotion, elle a dit : « Je vous aime, et je veux revenir ici pour construire un orphelinat pour ces magnifiques enfants. » Quelques minutes plus tard, la terre a tremblé. Britney a perdu la vie dans les décombres, mais son rêve n'est pas mort. Ses parents, Len et Cherylann Gengel, ont décidé de réaliser son vœu. Ils ont fondé la Fondation Be Like Brit et ont construit un orphelinat sûr, résistant aux séismes, au sommet d'une montagne à Grand‑Goâve, surplombant la route nationale #2. Le bâtiment a la forme d'un « B » – pour Brit. Aujourd'hui, des dizaines d'enfants y vivent, apprennent et jouent, entourés d'amour et de chances. Voici l'histoire d'une jeune fille qui a rêvé de donner un foyer, et d'une communauté qui a fait de ce rêve une réalité.",
        "caption": "L'orphelinat Be Like Brit vu du ciel – une forme de 'B' sur la montagne"
    },
    {
        "title": "Chapitre 2 : Le premier jour d'école",
        "image": chapters_en[1]["image"],
        "text": "La cloche sonna à 7h30. Jean‑Pierre, neuf ans, n'était jamais allé à l'école auparavant. Il tenait fermement son nouveau sac à dos, un cadeau des parents de la maison. La salle de classe était simple – des bureaux en bois, un tableau noir et une carte d'Haïti au mur. Son enseignante, Madame Claire, lui sourit. « Bonjour, Jean‑Pierre. Aujourd'hui, tu vas apprendre à écrire ton nom. » Il était nerveux, mais les autres enfants partagèrent leurs crayons de couleur avec lui. À la fin de la journée, il savait écrire « Jean‑Pierre » en grandes lettres bleues. Il courut montrer aux autres enfants. « Regardez ce que j'ai fait ! » s'écria‑t‑il. Ce soir‑là, il promit de devenir un jour ingénieur. Il voulait construire des écoles pour d'autres enfants comme lui. Son voyage avait commencé par une seule lettre.",
        "caption": "Enfants apprenant dans une salle de classe lumineuse"
    },
    {
        "title": "Chapitre 3 : Le jardin de l'espoir",
        "image": chapters_en[2]["image"],
        "text": "Derrière l'orphelinat se trouvait un petit jardin. Il était envahi par les mauvaises herbes, mais les enfants virent son potentiel. Guidés par leur mentor Jonas, ils décidèrent d'en faire un jardin potager. « Nous allons cultiver notre propre nourriture », dit‑il. Chaque après‑midi, ils creusaient la terre, semaient des graines et arrosaient les jeunes plants. La première semaine fut dure ; leurs mains se salissaient et leurs dos étaient courbatus. Mais ils travaillèrent ensemble. Rose, une fillette de douze ans, aimait voir apparaître les petites pousses. « Elles ressemblent à des petits soldats qui se frayent un chemin vers le soleil », dit‑elle. Deux mois plus tard, ils récoltèrent des tomates, des carottes et des haricots. La cuisinière les utilisa pour préparer un délicieux ragoût. Tous mangèrent ensemble, fiers de ce qu'ils avaient cultivé. Le jardin devint un symbole de leur force : même dans un sol difficile, de belles choses peuvent pousser.",
        "caption": "Enfants travaillant ensemble dans un jardin"
    },
    {
        "title": "Chapitre 4 : Une lettre de loin",
        "image": chapters_en[3]["image"],
        "text": "Un jour, une lettre arriva à l'orphelinat. Elle venait d'une étudiante de Boston qui avait entendu parler de Be Like Brit. Elle s'appelait Sarah et voulait devenir correspondante avec l'un des enfants. La directrice choisit Elie, un garçon calme de 14 ans qui aimait dessiner. Elie écrivit sa première lettre en français soigné : « Je m'appelle Elie. J'aime dessiner des oiseaux. Quel est ton animal préféré ? » Des semaines passèrent, et une réponse arriva. Sarah envoya des photos de la ligne d'horizon de Boston et un dessin de perroquet. Elie était ravi. Il se mit à dessiner chaque jour, avec le projet de devenir artiste. Leurs lettres allèrent et vinrent pendant des années. L'art d'Elie s'améliora, et il apprit l'anglais grâce aux notes de Sarah. Un jour, il déclara : « Un ami de l'autre côté de l'océan a cru en moi. Maintenant, je crois en moi-même. »",
        "caption": "Un enfant écrivant une lettre à la lueur d'une lampe"
    },
    {
        "title": "Chapitre 5 : Le grand match",
        "image": chapters_en[4]["image"],
        "text": "Le football était le cœur battant de l'orphelinat. Chaque samedi, les plus grands défiaient les plus jeunes lors d'un match amical. Cette fois, le prix était un trophée tout neuf offert par un visiteur. L'équipe des grands était confiante – elle avait la taille et l'expérience. Mais les plus jeunes avaient la vitesse et la faim. Le match fut intense. À cinq minutes de la fin, le score était de 2–2. Le petit Joseph, âgé de dix ans, reçut une passe près du but. Il ferma les yeux et tira. Le ballon fila directement dans le filet. Les plus jeunes explosèrent de joie. Joseph fut porté sur les épaules. Ce soir‑là, le trophée fut placé dans la salle commune. Joseph déclara : « Nous avons prouvé que la taille n'a pas d'importance. Ce qui compte, c'est la grandeur de votre cœur. » Les grands lui serrèrent la main et sourirent. Tout le monde fut gagnant ce jour‑là.",
        "caption": "Enfants jouant au football dans un champ"
    },
    {
        "title": "Chapitre 6 : L'art de donner",
        "image": chapters_en[5]["image"],
        "text": "Noël approchait, et les enfants étaient excités. Mais au lieu de demander des cadeaux, ils décidèrent de donner. Ils fabriquèrent des cartes et des bracelets faits à la main. Ils répétèrent des chants dans la chorale de l'église. La veille de Noël, ils visitèrent une maison de retraite voisine. Les résidents âgés n'avaient plus de famille. Les enfants chantèrent des cantiques, distribuèrent leurs créations et s'assirent auprès des vieilles personnes. Un vieil homme nommé Pierre pleura de joie. « Je n'ai pas eu de visite depuis des années, dit‑il. Vous êtes des anges. » Les enfants rentrèrent chez eux le cœur plein. Cette année‑là, ils apprirent que donner est un cadeau en soi. Une enfant, Mirlande, dit : « Nous avons si peu, mais nous pouvons quand même partager. C'est ça la vraie magie de Noël. »",
        "caption": "Enfants partageant des cadeaux avec des personnes âgées"
    },
    {
        "title": "Chapitre 7 : La tempête",
        "image": chapters_en[6]["image"],
        "text": "Un ouragan approchait. Le ciel s'assombrit et le vent hurlait. Les enfants avaient peur. Les parents de la maison les rassemblèrent dans la grande salle. Ils allumèrent des bougies et racontèrent des histoires pour les garder calmes. Pendant deux jours, la pluie tomba et le vent secoua les murs. Mais le bâtiment tint bon, grâce aux ingénieurs qui l'avaient construit. Lorsque la tempête passa, les enfants virent que le jardin était détruit et que quelques arbres étaient tombés. Mais ils étaient tous vivants. Ils travaillèrent ensemble pour nettoyer. Ils plantèrent de nouvelles graines dans le jardin. « Les tempêtes viendront, dit Jonas, mais nous sommes plus forts que n'importe quelle tempête. » Les enfants comprirent que la maison n'est pas seulement faite de murs ; ce sont les gens à l'intérieur.",
        "caption": "Un ouragan vu à travers une fenêtre"
    },
    {
        "title": "Chapitre 8 : Le visiteur",
        "image": chapters_en[7]["image"],
        "text": "Un après‑midi, une voiture s'arrêta devant la grille. Un grand homme en costume en descendit. C'était un cinéaste américain. Il avait entendu parler de Be Like Brit et voulait faire un documentaire. Les enfants étaient timides au début, mais ils s'ouvrirent bientôt. Ils lui montrèrent leurs œuvres d'art, leur terrain de football, leur jardin. Il les filma en train de rire, d'étudier et de s'entraider. Lorsque le documentaire sortit, des gens du monde entier virent le courage des enfants. Les dons affluèrent. Un nouveau dortoir fut construit. Les enfants apprirent que leur histoire avait du pouvoir. « Nous ne sommes pas seulement des victimes, dit l'un des garçons plus âgés, nous sommes les héros de notre propre vie. » Le cinéaste resta en contact et revint chaque année.",
        "caption": "Un cinéaste interviewant un enfant"
    },
    {
        "title": "Chapitre 9 : Le jour de la graduation",
        "image": chapters_en[8]["image"],
        "text": "Marie, maintenant âgée de 18 ans, avait terminé l'école. Elle se tenait sur une petite estrade dans la cour, vêtue d'une robe blanche. Tous les enfants, le personnel et quelques voisins s'étaient rassemblés. La mère de la maison lui remit un diplôme. Marie prononça un discours. « Quand je suis arrivée ici, je ne pouvais même pas parler. J'avais peur de tout. Mais vous m'avez donné une famille. Vous m'avez donné une éducation. Vous m'avez donné de l'espoir. » Elle envisageait d'étudier les soins infirmiers à l'université. Elle serait la première de sa classe à aller à l'université. Les plus jeunes enfants l'encouragèrent. Ils virent qu'un jour, eux aussi pourraient traverser cette scène. Marie serra chacun dans ses bras. « Je reviendrai, promit‑elle. J'aiderai ceux qui viendront après moi. » Son voyage ne faisait que commencer, mais elle avait déjà parcouru un si long chemin.",
        "caption": "Un diplômé fier tenant un certificat"
    },
    {
        "title": "Chapitre 10 : Un avenir radieux",
        "image": chapters_en[9]["image"],
        "text": "Aujourd'hui, les enfants de Be Like Brit sont médecins, infirmiers, enseignants, artistes et ingénieurs. Ils vivent en Haïti et à l'étranger, mais ils n'oublient jamais d'où ils viennent. Chaque année, à l'anniversaire de l'orphelinat, beaucoup reviennent. Ils jouent au football avec les nouveaux enfants, partagent des repas et racontent leurs propres voyages. Le jardin produit encore des légumes. La salle de classe résonne encore de leçons. Les murs restent solides, comme l'amour qui les a construits. Le voyage des enfants de Be Like Brit n'est pas seulement une question de survie. C'est une question d'épanouissement. C'est prendre une petite graine d'espoir et la nourrir jusqu'à ce qu'elle devienne un arbre qui ombragera beaucoup de gens. Et l'histoire continue, à chaque nouvel enfant qui franchit la grille.",
        "caption": "Enfants levant les mains avec espoir"
    }
]

# ---------- CHAPTERS: SPANISH ----------
chapters_es = [
    {
        "title": "Ubicación de Be Like Brit en la montaña en Grand‑Goâve carretera nacional #2",
        "image": chapters_en[0]["image"],
        "text": "Britney Gengel era una joven estadounidense que se enamoró de Haití y sus niños. Durante un viaje misionero en enero de 2010, llamó a sus padres por teléfono celular justo antes de que el devastador terremoto golpeara. Con voz entrecortada, dijo: «Los quiero, y quiero regresar aquí para construir un orfanato para estos hermosos niños». Unos minutos después, la tierra tembló. Britney perdió la vida entre los escombros, pero su sueño no murió. Sus padres, Len y Cherylann Gengel, decidieron hacer realidad su deseo. Fundaron la Fundación Be Like Brit y construyeron un orfanato seguro y resistente a terremotos en la cima de una montaña en Grand‑Goâve, con vista a la carretera nacional #2. El edificio tiene forma de «B» – por Brit. Hoy, decenas de niños viven, aprenden y juegan allí, rodeados de amor y oportunidades. Esta es la historia de una joven que soñó con dar un hogar, y de una comunidad que hizo ese sueño realidad.",
        "caption": "El orfanato Be Like Brit visto desde arriba – una forma de 'B' en la montaña"
    },
    {
        "title": "Capítulo 2: El primer día de escuela",
        "image": chapters_en[1]["image"],
        "text": "La campana sonó a las 7:30 a.m. Jean‑Pierre, de nueve años, nunca había ido a la escuela antes. Sostenía con fuerza su nueva mochila, un regalo de los padres de la casa. El aula era sencilla – pupitres de madera, una pizarra y un mapa de Haití en la pared. Su maestra, Madame Claire, le sonrió. «Buenos días, Jean‑Pierre. Hoy aprenderás a escribir tu nombre». Estaba nervioso, pero los otros niños compartieron sus crayones con él. Al final del día, podía escribir «Jean‑Pierre» en grandes letras azules. Corrió a mostrárselo a los demás niños. «¡Mira lo que hice!», gritó. Esa noche, prometió convertirse algún día en ingeniero. Quería construir escuelas para otros niños como él. Su viaje había comenzado con una sola letra.",
        "caption": "Niños aprendiendo en un aula luminosa"
    },
    {
        "title": "Capítulo 3: El jardín de la esperanza",
        "image": chapters_en[2]["image"],
        "text": "Detrás del orfanato había un pequeño jardín. Estaba cubierto de maleza, pero los niños vieron su potencial. Guiados por su mentor Jonas, decidieron convertirlo en un huerto. «Cultivaremos nuestra propia comida», dijo. Cada tarde cavaban la tierra, sembraban semillas y regaban las plantas jóvenes. La primera semana fue dura; sus manos se ensuciaban y sus espaldas dolían. Pero trabajaron juntos. Rose, una niña de doce años, amaba ver aparecer los pequeños brotes. «Parecen pequeños soldados abriéndose camino hacia el sol», dijo. Dos meses después, cosecharon tomates, zanahorias y frijoles. La cocinera los usó para hacer un delicioso guiso. Todos comieron juntos, orgullosos de lo que habían cultivado. El jardín se convirtió en un símbolo de su fuerza: incluso en tierra dura, las cosas hermosas pueden florecer.",
        "caption": "Niños trabajando juntos en un jardín"
    },
    {
        "title": "Capítulo 4: Una carta desde lejos",
        "image": chapters_en[3]["image"],
        "text": "Un día llegó una carta al orfanato. Era de una estudiante universitaria de Boston que había oído hablar de Be Like Brit. Se llamaba Sarah y quería ser amiga por correspondencia de uno de los niños. La directora eligió a Elie, un chico tranquilo de 14 años al que le encantaba dibujar. Elie escribió su primera carta en francés cuidadoso: «Me llamo Elie. Me gusta dibujar pájaros. ¿Cuál es tu animal favorito?». Pasaron semanas y llegó una respuesta. Sarah envió fotos del horizonte de Boston y un dibujo de un loro. Elie se llenó de alegría. Comenzó a dibujar todos los días, con la intención de convertirse en artista. Sus cartas fueron y vinieron durante años. El arte de Elie mejoró y aprendió inglés gracias a las notas de Sarah. Un día dijo: «Una amiga al otro lado del océano creyó en mí. Ahora yo creo en mí mismo».",
        "caption": "Un niño escribiendo una carta a la luz de una lámpara"
    },
    {
        "title": "Capítulo 5: El gran partido",
        "image": chapters_en[4]["image"],
        "text": "El fútbol era el corazón del orfanato. Cada sábado, los mayores desafiaban a los menores a un partido amistoso. Esta vez, el premio era un flamante trofeo donado por un visitante. El equipo de los mayores estaba confiado – tenían altura y experiencia. Pero los menores tenían velocidad y hambre. El partido fue intenso. A cinco minutos del final, el marcador era 2–2. El pequeño Joseph, de apenas diez años, recibió un pase cerca de la portería. Cerró los ojos y pateó. El balón voló directamente a la red. El equipo menor estalló en vítores. Joseph fue llevado en hombros. Esa noche, el trofeo se colocó en la sala común. Joseph dijo: «Demostramos que el tamaño no importa. Lo que importa es el tamaño de tu corazón». Los mayores le dieron la mano y sonrieron. Todos fueron ganadores ese día.",
        "caption": "Niños jugando al fútbol en un campo"
    },
    {
        "title": "Capítulo 6: El arte de dar",
        "image": chapters_en[5]["image"],
        "text": "Se acercaba la Navidad y los niños estaban emocionados. Pero en lugar de pedir regalos, decidieron dar. Hicieron tarjetas y pulseras hechas a mano. Ensayaron canciones en el coro de la iglesia. En Nochebuena, visitaron un asilo cercano. Los ancianos residentes no tenían familia. Los niños cantaron villancicos, entregaron sus manualidades y se sentaron con los mayores. Un anciano llamado Pierre lloró de alegría. «No me habían visitado en años», dijo. «Son ángeles». Los niños regresaron a casa con el corazón lleno. Ese año aprendieron que dar es un regalo en sí mismo. Una niña, Mirlande, dijo: «Tenemos tan poco, pero aún podemos compartir. Esa es la verdadera magia de la Navidad».",
        "caption": "Niños compartiendo regalos con ancianos"
    },
    {
        "title": "Capítulo 7: La tormenta",
        "image": chapters_en[6]["image"],
        "text": "Se acercaba un huracán. El cielo se oscureció y el viento aullaba. Los niños estaban asustados. Los padres de la casa los reunieron en el salón principal. Encendieron velas y contaron historias para mantenerlos calmados. Durante dos días, la lluvia cayó y el viento sacudió las paredes. Pero el edificio se mantuvo firme, gracias a los ingenieros que lo construyeron. Cuando pasó la tormenta, los niños vieron que el jardín estaba destruido y que algunos árboles habían caído. Pero todos estaban vivos. Trabajaron juntos para limpiar. Plantaron nuevas semillas en el jardín. «Las tormentas llegarán», dijo Jonas, «pero somos más fuertes que cualquier tormenta». Los niños entendieron que el hogar no son solo paredes; son las personas que hay dentro.",
        "caption": "Un huracán visto a través de una ventana"
    },
    {
        "title": "Capítulo 8: El visitante",
        "image": chapters_en[7]["image"],
        "text": "Una tarde, un coche se detuvo en la puerta. Un hombre alto vestido con traje bajó. Era un cineasta de Estados Unidos. Había oído hablar de Be Like Brit y quería hacer un documental. Los niños eran tímidos al principio, pero pronto se abrieron. Le mostraron su arte, su campo de fútbol, su jardín. Los filmó riendo, estudiando y ayudándose mutuamente. Cuando se estrenó el documental, personas de todo el mundo vieron el coraje de los niños. Llegaron donaciones. Se construyó un nuevo dormitorio. Los niños aprendieron que su historia tenía poder. «No somos solo víctimas», dijo uno de los chicos mayores, «somos héroes de nuestras propias vidas». El cineasta mantuvo el contacto y regresó cada año.",
        "caption": "Un cineasta entrevistando a un niño"
    },
    {
        "title": "Capítulo 9: Día de graduación",
        "image": chapters_en[8]["image"],
        "text": "Marie, ahora de 18 años, había terminado la escuela. Estaba en un pequeño escenario en el patio, con un vestido blanco. Todos los niños, el personal y algunos vecinos se habían reunido. La madre de la casa le entregó un certificado. Marie dio un discurso. «Cuando llegué aquí, ni siquiera podía hablar. Tenía miedo de todo. Pero ustedes me dieron una familia. Me dieron una educación. Me dieron esperanza». Planeaba estudiar enfermería en la universidad. Sería la primera de su grupo en ir a la universidad. Los niños más pequeños la animaron. Vieron que algún día ellos también podrían cruzar ese escenario. Marie abrazó a cada uno de ellos. «Volveré», prometió. «Ayudaré a los que vengan después de mí». Su viaje apenas comenzaba, pero ya había recorrido un largo camino.",
        "caption": "Un graduado orgulloso sosteniendo un certificado"
    },
    {
        "title": "Capítulo 10: Un futuro brillante",
        "image": chapters_en[9]["image"],
        "text": "Hoy, los niños de Be Like Brit son médicos, enfermeros, maestros, artistas e ingenieros. Viven en Haití y en el extranjero, pero nunca olvidan de dónde vienen. Cada año, en el aniversario del orfanato, muchos regresan. Juegan al fútbol con los nuevos niños, comparten comidas y cuentan historias de sus propios viajes. El jardín todavía produce verduras. El aula todavía resuena con lecciones. Las paredes todavía se mantienen firmes, como el amor que las construyó. El viaje de los niños de Be Like Brit no es solo sobre la supervivencia. Es sobre prosperar. Es tomar una pequeña semilla de esperanza y alimentarla hasta que se convierta en un árbol que dé sombra a muchos. Y la historia continúa, con cada nuevo niño que cruza la puerta.",
        "caption": "Niños levantando las manos con esperanza"
    }
]

# ---------- MAP LANGUAGE TO CHAPTERS ----------
language_map = {
    "en": chapters_en,
    "fr": chapters_fr,
    "es": chapters_es
}

# ---------- CUSTOM CSS (LIGHT BLUE BACKGROUND – SAME AS GlobalInternet.py) ----------
st.markdown("""
<style>
    /* Light blue background for the whole app */
    .stApp {
        background: linear-gradient(135deg, #e0f0ff 0%, #b8d9ff 100%) !important;
    }
    /* Sidebar slightly darker for contrast */
    [data-testid="stSidebar"] {
        background-color: rgba(200, 220, 250, 0.95) !important;
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .lesson-card {
        background-color: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        border-left: 5px solid #2a5298;
    }
    .lesson-card:hover { transform: translateY(-5px); }
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #1e2a3e;
        text-align: justify;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #d4e4ff;
        border-radius: 20px;
        color: #1e3c72;
    }
    .sidebar-image {
        display: block;
        width: 100%;
        max-width: 200px;
        margin: 0 auto 1rem auto;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #ff4444;
        border-radius: 50%;
        animation: pulse 1.2s infinite;
        margin-right: 8px;
        vertical-align: middle;
    }
    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }
    .reading-indicator {
        display: inline-flex;
        align-items: center;
        background: #f0f0f0;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    h1, h2, h3 {
        color: #1e3c72;
    }
    .stButton button {
        background-color: #2a5298;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #1e3c72;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# ---------- LANGUAGE SELECTOR IN SIDEBAR ----------
lang_options = {
    "English": "en",
    "Français": "fr",
    "Español": "es"
}
selected_lang_name = st.sidebar.selectbox(
    _("language_selector"),
    list(lang_options.keys()),
    index=["en","fr","es"].index(st.session_state.lang)
)
st.session_state.lang = lang_options[selected_lang_name]
chapters = language_map[st.session_state.lang]

# ---------- SIDEBAR CONTENT (IMAGE + LINK + BOOK INFO) ----------
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/Deslandes1/The-Journey-of-the-Be-Like-Brit-Kids/main/badg.jpg",
        use_container_width=True,
        caption=""
    )
    st.markdown("---")
    st.markdown(f"[{_('sidebar_website')}](https://belikebrit.org/)")
    st.markdown("---")
    st.markdown(f"### {_('sidebar_book_title')}")
    st.markdown(_("sidebar_book_desc"))
    st.markdown("---")
    st.caption(_("sidebar_caption"))

# ---------- MAIN PAGE ----------
def main():
    st.markdown(
        f"""
        <div class="main-header">
            <h1>{_("app_title")}</h1>
            <p>{_("app_sub")}</p>
            <p style="font-size:0.9rem; margin-top:0.5rem; opacity:0.9;">{_("app_authors")}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    chapter_titles = [f"{i+1}. {ch['title']}" for i, ch in enumerate(chapters)]
    selected_idx = st.sidebar.selectbox(_("chapter_selector"), range(len(chapters)), format_func=lambda i: chapter_titles[i])
    
    chapter = chapters[selected_idx]
    
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        col_img, col_text = st.columns([1, 2])
        with col_img:
            st.image(chapter['image'], caption=chapter.get('caption', 'Illustration'), use_container_width=True)
        with col_text:
            st.markdown(f"## {chapter['title']}")
            st.markdown(f'<div class="story-text">{chapter["text"]}</div>', unsafe_allow_html=True)
            
            read_btn = st.button(f"{_('read_aloud_button')} ({selected_idx+1})", key=f"read_{selected_idx}")
            if read_btn:
                indicator = st.empty()
                indicator.markdown(
                    f'<div class="reading-indicator"><span class="pulse-dot"></span> {_("reading_indicator")}</div>',
                    unsafe_allow_html=True
                )
                text_to_speak = chapter["text"].replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                lang_code = {"en": "en-US", "fr": "fr-FR", "es": "es-ES"}[st.session_state.lang]
                js_code = f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                    utterance.lang = "{lang_code}";
                    utterance.onend = function() {{
                        var event = new CustomEvent('streamlit:setComponentValue', {{detail: {{value: "done"}}}});
                        window.dispatchEvent(event);
                    }};
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """
                components.html(js_code, height=0)
                st.success(_("reading_success"))
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} {_('footer_copyright')}</p>
        <p>{_('footer_book')}</p>
        <p>{_('footer_built')}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
