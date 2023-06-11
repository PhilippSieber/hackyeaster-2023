from flask import Flask 
import random 

app = Flask(__name__)

quotes = ["Don't let yesterday take up too much of today. ~ Will Rogers",
"If you're going through hell, keep going. ~ Winston Churchill",
"Every man dies. Not every man lives. ~ William Wallace",
"Life shrinks or expands in proportion to one's courage. ~ Anais Nin",
"Nothing is impossible. The word itself says I'm possible! ~ Audrey Hepburn",
"We need much less than we think we need. ~ Maya Angelou",
"Everything has beauty, but not everyone sees it. ~ Confucius",
"Simplicity is the ultimate sophistication. ~ Leonardo da Vinci",
"There is no way to happiness - happiness is the way. ~ Thich Nhat Hanh",
"Whatever you are, be a good one. ~ Abraham Lincoln",
"Be yourself; everyone else is already taken. ~ Oscar Wilde",
"Act as if what you do makes a difference. It does. ~ William James",
"The only real mistake is the one from which we learn nothing. ~  Henry Ford",
"Positive anything is better than negative nothing. ~ Elbert Hubbard",
"Limit your 'always' and your 'nevers'. ~ Amy Poehler",
"Creativity is intelligence having fun. ~ Albert Einstein",
"If you tell the truth you don't have to remember anything. ~ Mark Twain",
"Be so good they can't ignore you. ~ Steve Martin",
"There is no substitute for hard work. ~ Thomas Edison",
"Try to be a rainbow in someone else's cloud. ~ Maya Angelou",
"You do not find the happy life. You make it. ~ Camilla Eyring Kimball",
"Sometimes you will never know the value of a moment, until it becomes a memory. ~ Dr. Seuss",
"Happiness depends upon ourselves. ~ Aristotle",
"If you look at what you have in life, you'll always have more. ~ Oprah Winfrey",
"Yesterday's the past, tomorrow's the future, but today is a gift. That's why it's called the present. ~ Bil Keane",
"Time moves in one direction, memory in another. ~ William Gibson",
"Lose an hour in the morning, and you will spend all day looking for it. ~ Richard Whately",
"To improve is to change; to be perfect is to change often. ~ Winston Churchill",
"Every accomplishment starts with the decision to try. ~ Brian Littrell",
"Every moment is a fresh beginning. ~ T.S Eliot",
"Never regret anything that made you smile. ~ Mark Twain",
"Dream as if you'll live forever, live as if you'll die today.  ~ James Dean",
"All limitations are self-imposed. ~ Oliver Wendell Holmes",
"Life is like riding a bicycle. To keep your balance, you must keep moving. ~ Albert Einstein",
"Problems are not stop signs, they are guidelines. ~ Robert H. Schiuller",
"Success is not final, failure is not fatal: it is the courage to continue that counts. ~ Winston Churchill",
"Believe you can and you're halfway there. ~ Theodore Roosevelt",
"No matter what you're going through, there's a light at the end of the tunnel. ~ Demi Lovato",
"What we think, we become. ~ Buddha",
"It is never too late to be what you might have been. ~ George Eliot",
"Happiness often sneaks in through a door you didn't know you left open. ~ John Barrymore",
"Happiness is not by chance, but by choice. ~ Jim Rohn",
"Life changes very quickly, in a very positive way, if you let it. ~ Lindsey Vonn",
"Keep your face to the sunshine and you cannot see a shadow. ~ Helen Keller",
"Be the change that you wish to see in the world. ~ Mahatma Gandhi",
"If I cannot do great things, I can do small things in a great way. ~ Martin Luther King Jr.",
"The bad news is time flies. The good news is you're the pilot. ~ Michael Altshuler",
"Don't wait. The time will never be just right. ~ Napoleon Hillf",
"No matter what people tell you, words and ideas can change the world. ~ Robin Williams",
"You cannot explore the universe if you think that you are the center of it. ~ Joshua Suya Pelicano",
"Action may not always bring happiness; but there is no happiness without action. ~ Benjamin Disraeli",
"You can't cross the sea merely by standing and staring at the water. ~ Rabindranath Tagore",
"Life is 10% what happens to you and 90% how you react to it. ~ Charles R. Swindoll",
"We may encounter many defeats but we must not be defeated. ~ Maya Angelou",
"Life isn't about finding yourself. Life is about creating yourself. ~ George Bernard Shaw",
"Be happy for this moment. This moment in your life. ~ Omar Khayyam",
"If you can dream it, you can do it. ~ Walt Disney",
"Rise above the storm and you will find the sunshine. ~ Mario Fernández",
"If opportunity doesn't knock, build a door. ~ Milton Berle",
"Life becomes easier when you learn to accept the apology you never got. ~ R. Brault",
"It hurt because it mattered. ~ John Green",
"Happiness is not something ready-made. It comes from your own actions. ~ Dalai Lama",
"Life is really simple, but we insist on making it complicated. ~  Confucius",
"The road to success is always under construction. ~ Lily Tomlin",
"To live is the rarest thing in the world. Most people just exist. ~ Oscar Wilde",
"A person who never made a mistake never tried anything new. ~ Albert Einstein",
"Doubt kills more dreams than failure ever will. ~ Suzy Kassem",
"Despite the forecast, live like it's spring. ~ Lily Pulitzer",
"It always seems impossible until it's done. ~ Nelson Mandela",
"When we give cheerfully and accept gratefully, everyone is blessed. ~ Maya Angelou",
"Everything you've ever wanted is on the other side of fear. ~ George Addair",
"If you have the ability to love, love yourself first. ~ Charles Bukowski",
"Never, never, never give up. ~ Winston Churchill",
"Either you run the day, or the day runs you. ~ Jim Rohn",
"The shortest answer is doing. ~ Lord Herbert",
"Knowledge speaks, but wisdom listens. ~ Jimi Hendrix",
"Don't cry because it's over. Smile because it happened. ~ Dr. Seuss",
"In life you need either inspiration or desperation. ~ Tony Robbins",
"No one can make you feel inferior without your consent. ~ Eleanor Roosevelt",
"Be not afraid of going slowly, be afraid only of standing still. ~ Chinese Proverb",
"Those who dare to fail miserably can achieve greatly. ~ John F. Kennedy",
"Mastering others is strength. Mastering yourself is true power. ~ Lao Tzu",
"Die with good memories, not with unfulfilled dreams. ~ Invajy",
"I don't need it to be easy, I need it to be worth it. ~ Lil Wayne",
"Good things happen to those who hustle. ~ Anais Nin",
"Forget about style; worry about results. ~ Bobby Orr",
"The roots of education are bitter, but the fruit is sweet. ~:   Aristotle",
"You must be the change you wish to see in the world. ~ Mahatma Gandhi",
"To succeed in life, you need two things: ignorance and confidence. ~ Mark Twain",
"It's kind of fun to do the impossible. ~ Walt Disney",
"A place for everything, everything in its place. ~ Benjamin Franklin",
"Aspire to inspire before you expire. ~ Anonymous",
"The journey of a thousand miles begins with one step. ~ Lao Tzu",
"In the middle of difficulty lies opportunity. ~ Albert Einstein",
"Goal setting is the secret to a compelling future. ~ Tony Robbins",
"Energy and initiative count as much as talent and luck. ~ Will Peters",
"Goals help you channel your energy into action. ~ Les Brown",
"The key to life is not accumulation. It's contribution. ~ Stephen Covey",
"The most wasted of days is one without laughter. ~E.E. Cummings",
"Impossible is for the unwilling. ~ John Keats",
"No pressure, no diamonds. ~ Thomas Carlyle",
"Dream big and dare to fail. ~ Norman Vaughan",
"Excuses are the nails used to build a house of failure. ~ Jim Rohn",
"We can't help everyone, but everyone can help someone. ~ Ronald Reagan",
"Whether you think you can, or you think you can't - you're right. ~ Henry Ford",
"Don't wish it were easier. Wish you were better. ~ Jim Rohn",
"The best way out is always through. ~ Robert Frost",
"You miss 100% of the shots you don't take. ~ Wayne Gretzky",
"We will either find a way, or make one. ~ Hannibal",
"It is better to fail in originality than to succeed in imitation. ~ Herman Melville",
"Success usually comes to those who are too busy looking for it. ~ Henry David Thoreau",
"You can't live an exceptional life by being normal. ~ Nick Maley",
"I'm a slow walker, but I never walk back. ~ Abraham Lincoln",
"A wise man will make more opportunities than he finds. ~ Francis Bacon",
"There can be glory in failure and despair in success. ~ Abraham Lincoln",
"Belief creates the actual fact. ~ William James",
"Spread love everywhere you go. ~ Mother Teresa",
"Don't quit. Suffer now and live the rest of your life as a champion. ~ Muhammad Ali",
"Aim for the moon. If you miss, you may hit a star. ~ W. Clement Stone",
"It's not all over, till you have the courage to comeback. ~ Invajy",
"Dreaming, after all, is a form of planning. ~ Gloria Steinem",
"I would rather die of passion than of boredom. ~ Vincent van Gogh",
"It does not matter how slowly you go as long as you do not stop. ~ Confucius",
"An unexamined life is not worth living. ~ Socrates",
"Failures are foundation stones of the Success Forts ~ Invajy",
"You become what you believe. ~ Oprah Winfrey",
"Today, you have 100% of your life left. ~ Tom Landry",
"There are no regrets in life, just lessons. ~ Jennifer Aniston",
"Nothing is more honorable than a grateful heart. ~ Seneca",
"Worry causes stress, but care causes concern. ~ Chris Vail"]

stars = ["Alpha Canis Majoris","Alpha Carinae","Alpha Bootis","Alpha Centauri","Alpha Lyrae","Alpha Aurigae",
         "Beta Orionis","Alpha Canis Minoris","Alpha Orionis","Alpha Eridani","Beta Centauri","Alpha Aquilae",
         "Alpha Crucis","Alpha Tauri","Alpha Virginis","Alpha Scorpii","Beta Geminorum","Alpha Piscis Austrini",
         "Alpha Cygni","Beta Crucis","Alpha Leonis","Epsilon Canis Majoris","Alpha Geminorum","Gamma Crucis",
         "Lambda Scorpii","Gamma Orionis","Beta Tauri","Beta Carinae","Epsilon Orionis","Alpha Gruis","Zeta Orionis",
         "Gamma Velorum","Epsilon Ursae Majoris","Epsilon Sagittarii","Alpha Persei","Alpha Ursae Majoris",
         "Delta Canis Majoris","Eta Ursae Majoris","Theta Scorpii","Epsilon Carinae","Beta Aurigae",
         "Alpha Trianguli Australis","Delta Velorum","Gamma Geminorum","Alpha Pavonis","Alpha Ursae Minoris",
         "Beta Canis Majoris","Alpha Hydrae","Gamma Leonis","Alpha Arietis","Beta Ceti",
         "Sigma Sagittarii","Theta Centauri","Kappa Orionis","Alpha Andromedae","Beta Gruis","Beta Andromedae",
         "Beta Ursae Minoris","Alpha Ophiuchi","Beta Persei","Gamma Andromedae","Beta Leonis","Gamma Cassiopeiae",
         "Gamma Centauri","Zeta Puppis","Iota Carinae","Alpha Coronae Borealis","Lambda Velorum","Gamma Cygni",
         "Zeta Ursae Majoris","Alpha Cassiopeiae","Gamma Draconis","Delta Orionis","Beta Cassiopeiae","Delta Scorpii",
         "Epsilon Scorpii","Epsilon Centauri","Alpha Lupi","Eta Centauri","Beta Ursae Majoris","Epsilon Bootis",
         "Epsilon Pegasi","Kappa Scorpii","Alpha Phoenicis","Gamma Ursae Majoris","Eta Ophiuchi","Beta Pegasi",
         "Alpha Cephei","Eta Canis Majoris","Kappa Velorum","Epsilon Cygni","Alpha Pegasi","Zeta Ophiuchi",
         "Alpha Ceti","Zeta Centauri","Beta Scorpii","Delta Leonis","Delta Centauri","Alpha Leporis","Gamma Corvi"]

colors = ["Alice blue","Antique white","Aqua","Aquamarine","Azure","Beige","Bisque","Black","Blanched almond",
          "Blue","Blue violet","Brown","Burlywood","Cadet blue","Chartreuse","Chocolate","Coral","Cornflower blue",
          "Cornsilk","Crimson","Cyan","Dark blue","Dark cyan","Dark goldenrod","Dark gray","Dark green","Dark khaki",
          "Dark magenta","Dark olive green","Dark orange","Dark orchid","Dark red","Dark salmon","Dark seagreen",
          "Dark slate blue","Dark slate gray","Dark turquoise","Dark violet","Deep pink","Deep sky blue","Dim gray",
          "Dodger blue","Firebrick","Floral white","Forest green","Fuchsia","Gainsboro","Ghost white","Gold","Goldenrod",
          "Gray","Green","Green yellow","Honeydew","Hot pink","Indian red","Indigo","Ivory","Khaki","Lavender",
          "Lavender blush","Lawn green","Lemon chiffon","Light blue","Light coral","Light cyan","Light goldenrod yellow",
          "Light green","Light grey","Light pink","Light salmon","Light sea green","Light sky blue","Light slate gray",
          "Light steel blue","Light yellow","Lime","Lime green","Linen","Magenta","Maroon","Medium aquamarine",
          "Medium blue","Medium orchid","Medium purple","Medium sea green","Medium slate blue","Medium spring green",
          "Medium turquoise","Medium violet red","Midnight blue","Mint cream","Misty rose","Moccasin","Navajo white",
          "Navy","Old lace","Olive drab","Orange","Orange red"]

cheese = ["Applewood cheese","Ashdown Foresters","Bath Blue","Bath Soft Cheese",
          "Beacon Fell Traditional Lancashire Cheese","Beenleigh Blue cheese","Berkswell","Blue Stilton","Black Bomber",
          "Bowland cheese","Brighton Blue","Buxton Blue","Cheddar","Cheshire","Chevington","Colwick","Coquetdale",
          "Cornish Blue","Cornish Brie","Cornish Yarg","Coverdale","Croglin","Davidstow Cheddar","Derby",
          "Dorset Blue Vinney","Dorset Drum","Dovedale cheese","Duddleswell cheese","Fine Fettle Yorkshire",
          "Gevrik","Gloucester","Harbourne Blue","Hereford Hop","Lancashire","Lincolnshire Poacher cheese","Little Derby",
          "Lymeswold cheese","Keltic Gold","Marble cheese","Merry Wyfe (Bath)","Norbury Blue","Old Winchester",
          "Oxford Blue (cheese)","Parlick Fell cheese","Red Leicester","Red Windsor","Renegade Monk","Sage Derby",
          "Shropshire Blue","Stichelton","Stilton","Blue Stilton","White Stilton","Stinking Bishop","St James Cheese",
          "Suffolk Gold","Suffolk Bang","Sussex Slipcote","Swaledale","Tesyn","Waterloo cheese","Wensleydale",
          "Wyfe of Bath (Bath)"]

wine = ["Ajaccio","Aloxe-Corton","Alsace Grand Cru","Anjou","Anjou-Coteaux de la Loire","Anjou-Gamay","Anjou mousseux",
        "Anjou Villages","Anjou Villages Brissac","Arbois","Auxey-Duresses","Bandol","Banyuls","Banyuls Grand Cru","Barsac",
        "Bâtard-Montrachet","Béarn","Beaujolais-Villages","Beaumes de Venise","Beaune","Bellet","Bergerac","Bergerac rosé",
        "Bergerac sec","Bienvenues-Bâtard-Montrachet","Blagny","Blanquette de Limoux","Blanquette méthode ancestrale","Blaye",
        "Bonnes-Mares","Bonnezeaux","Bordeaux clairet","Bordeaux Côtes de Francs","Bordeaux Haut-Benauge","Bordeaux moelleux",
        "Bordeaux rosé","Bordeaux sec","Bordeaux supérieur","Bourgogne","Bourgogne aligoté","Bourgogne clairet",
        "Bourgogne clairet Côte chalonnaise","Bourgogne Côte Saint-Jacques","Bourgogne Côtes d'Auxerre","Bourgogne Côtes du Couchois",
        "Bourgogne Coulanges-la-Vineuse","Bourgogne Epineuil","Bourgogne grand ordinaire","Bourgogne Hautes-côtes de Beaune",
        "Bourgogne Hautes-côtes de Nuits","Bourgogne La Chapelle Notre-Dame","Bourgogne le Chapitre","Bourgogne Montrecul",
        "Bourgogne mousseux","Bourgogne ordinaire","Bourgogne Passe-tout-grains","Bourgogne rosé","Bourgogne Vézelay","Bourgueil",
        "Bouzeron","Brouilly","Bugey","Buzet","Cabardes","Cabernet d'Anjou","Cabernet de Saumur","Cadillac","Cahors","Cairanne",
        "Cassis","Cérons","Chablis","Chablis Grand Cru","Chablis Premier Cru","Chambertin","Chambertin-Clos-de-Beze","Chambolle-Musigny",
        "Chapelle-Chambertin","Charlemagne","Charmes-Chambertin","Chassagne-Montrachet","Château-Chalon","Château-Grillet",
        "Châteauneuf-du-Pape","Châtillon-en-Diois","Chaume","Chénas","Chevalier-Montrachet","Cheverny","Chinon","Chiroubles",
        "Chorey-les-Beaune","Clairette de Bellegarde","Clairette de Die","Clairette du Languedoc","Clos de la Roche","Clos des Lambrays",
        "Clos de Tart","Clos de Vougeot","Clos Saint-Denis","Collioure","Condrieu","Corbieres","Cornas","Corton","Corton-Charlemagne",
        "Costières de Nîmes","Coteaux Champenois","Coteaux d'Aix-en-Provence","Coteaux de Die","Coteaux de l'Aubance","Coteaux de Pierrevert",
        "Coteaux de Saumur","Coteaux du Giennois","Coteaux du Languedoc","Coteaux du Layon","Coteaux du Loir","Coteaux du Lyonnais",
        "Coteaux du Quercy","Coteaux du Tricastin","Coteaux du Vendômois","Coteaux Varois","Côte de Beaune","Côte de Beaune-Villages",
        "Côte de Brouilly","Côte de Nuits-villages","Côte Roannaise","Côte-Rôtie","Côtes de Bergerac","Côtes de Bergerac Blanc",
        "Côtes de Blaye","Côtes de Bordeaux Saint-Macaire","Côtes de Bourg","Côtes de Castillon","Côtes de Duras","Côtes de la Malepere",
        "Côtes de Millau","Côtes de Montravel","Côtes de Provence","Côtes de Toul","Côtes du Forez","Côtes du Jura","Côtes du Luberon",
        "Côtes du Marmandais","Côtes du Rhône","Côtes du Rhône Villages","Côtes du Roussillon","Côtes du Roussillon Villages",
        "Côtes du Ventoux","Côtes du Vivarais","Cour-Cheverny","Crémant d'Alsace","Crémant de Bordeaux","Crémant de Bourgogne",
        "Crémant de Die","Crémant de Limoux","Crémant de Loire","Crémant du Jura","Crépy","Criots-Bâtard-Montrachet","Crozes-Hermitage",
        "Eastern France","Échezeaux","Entre-Deux-Mers","Entre-Deux-Mers-Haut-Benauge","Faugeres","Fitou","Fixin","Fleurie","Fronsac",
        "Frontignan","Fronton","Gaillac","Gaillac Premieres Côtess","Gevrey-Chambertin","Gigondas","Givry","Grand Roussillon",
        "Grands Échezeaux","Graves","Graves de Vayres","Graves Supérieures","Griotte-Chambertin","Haut-Médoc","Haut-Montravel",
        "Haut-Poitou","Hermitage","Irancy","Irouléguy","Jasnieres","Juliénas","Jurançon","Ladoix","La Grande Rue","Lalande-de-Pomerol",
        "Languedoc","La Romanée","La Tâche","Latricieres-Chambertin","Les Baux-de-Provence","L'Étoile","Limoux","Lirac","Listrac-Médoc",
        "Loupiac","Lussac-Saint-Émilion","Lyonnais","Mâcon","Mâcon supérieur","Mâcon-villages","Madiran","Maranges","Marcillac","Margaux",
        "Marsannay","Maury","Mazis-Chambertin","Mazoyeres-Chambertin","Médoc","Menetou-Salon","Mercurey","Meursault","Minervois",
        "Minervois-La Liviniere","Monbazillac","Montagne Saint-Émilion","Montagny","Monthelie","Montlouis","Montrachet","Montravel",
        "Morey-Saint-Denis","Morgon","Moulin a vent","Moulis-en-Médoc","Muscadet","Muscadet-Coteaux de la Loire","Muscadet-Côtes de Grandlieu",
        "Muscadet-Sevre et Maine","Muscat de Beaumes-de-Venise","Muscat de Frontignan","Muscat de Lunel","Muscat de Mireval",
        "Muscat de Rivesaltes","Muscat de Saint-Jean de Minervois","Musigny","Néac","Nuits-Saint-Georges","Orléans","Orléans-Cléry",
        "Pacherenc du Vic-Bilh","Pacherenc du Vic-Bilh Sec","Palette","Patrimonio","Pauillac","Pécharmant","Pernand-Vergelesses",
        "Pessac-Léognan","Petit Chablis","Pomerol","Pommard","Pouilly-Fuissé","Pouilly-Fumé","Pouilly-Loché","Pouilly-sur-Loire",
        "Pouilly-Vinzelles","Premieres Côtes de Blaye","Premieres Côtes de Bordeaux","Puisseguin Saint-Émilion","Puligny-Montrachet",
        "Quarts de Chaume","Quincy","Régnié","Reuilly","Rhone Valley","Richebourg","Rivesaltes","Romanée-Conti","Romanée-Saint-Vivant",
        "Rosé d'Anjou","Rosé de Loire","Rosé des Riceys","Rosette","Roussette de Savoie","Roussette du Bugey","Ruchottes-Chambertin",
        "Rully","Saint-Amour","Saint-Aubin","Saint-Bris","Saint-Chinian","Sainte-Croix-du-Mont","Sainte-Foy-Bordeaux","Saint-Émilion",
        "Saint-Émilion Grand Cru","Saint-Estephe","Saint-Georges Saint-Émilion","Saint-Joseph","Saint-Julien","Saint-Mont",
        "Saint-Nicolas-de-Bourgueil","Saint-Péray","Saint-Pourçain","Saint-Romain","Saint-Sardos","Saint-Véran","Sancerre","Santenay",
        "Saumur","Saumur-Champigny","Saumur mousseux","Saussignac","Sauternes","Savennières","Savennières-Coulée-de-Serrant",
        "Savennières-Roche-aux-Moines","Savigny-les-Beaune","Seyssel","Tavel","Tonnerre","Touraine","Touraine-Amboise",
        "Touraine-Azay-le-Rideau","Touraine-Mesland","Touraine Noble Joué","Tursan","Vacqueyras","Valençay","Vin de Corse",
        "Vin de Savoie","Vins d'Entraygues et du Fel","Vins d'Estaing","Vins Fins de la Côte de Nuits","Vinsobres","Viré-Clessé",
        "Volnay","Volnay Santenots","Vosne-Romanée","Vougeot","Vouvray"]

trek = ["Christopher Pike","Admiral James T. Kirk","Spock","Number One","Willard Decker","Hikaru Sulu","Montgomery Scott (Scotty)","Nyota Uhura",
        "Alec MacPherson","Leonard McCoy","Worf","Seven of Nine","Jean-Luc Picard","Benjamin Sisko","Data","Wesley Crusher","Beverly Crusher",
        "Quark","Lwaxana Troi","Miles O'Brien","Kathryn Janeway","Odo","Guinan","Elim Garak","Lt. Commander La Forge","Q","T'Pol","Deanna Troi",
        "Tom Paris","Chakotay"]

# ################
# Quote
# ################
@app.route("/quote")
def serveQuote():
    nr = random.randint(0, len(quotes))
    return quotes[nr]

# ################
# Color
# ################
@app.route("/color")
def serveColor():
    nr = random.randint(0, len(colors))
    return colors[nr]

# ################
# Star
# ################
@app.route("/star")
def serveStar():
    nr = random.randint(0, len(stars))
    return stars[nr]

# ################
# Cheese
# ################
@app.route("/cheese")
def serveCheese():
    nr = random.randint(0, len(cheese))
    return cheese[nr]

# ################
# Wine
# ################
@app.route("/wine")
def serveWine():
    nr = random.randint(0, len(wine))
    return wine[nr]

# ################
# Meals
# ################
@app.route("/meal")
def serveMeal():
    return "Fondue"

# ################
# Star Trek
# ################
@app.route("/trek")
def serveTrek():
    nr = random.randint(0, len(trek))
    return trek[nr]

# ################
# Flag
# ################
@app.route("/flag")
def serveFlag():
    return "Thank you hacker! But our flag is in another castle! ~ Bugs Bunny"

# ################
# Main  
# ################
if __name__ == "__main__":
    app.logger.info("App is started ...")
    app.run(debug=False, host="0.0.0.0", port="1337")
