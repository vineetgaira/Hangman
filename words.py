import requests
import colorama
import random
from colorama import Fore



WORDS = ["apotheosizing","bonspiel","deaired","sautoir","spiritedly","naturalizes","kevels","pere","thematically","cory","unwarier","outjumps","thralls",
         "selvages","fere","subtask","finca","hegiras","cresol","shtetl","deflector","checkerboard","anticlines","bibliomaniacal","retinal","empressements",
         "salutatorian","humidity","arrears","jammiest","typists","paesanos","corders","hemosiderins","rewetting","resinating","beachwear","beslimed","produce",
         "dackering","lamellately","vaporizations","acylate","skiffs","bathed","depeoples","gillying","skiffles","taros","histopathologic","crunchily","spearing",
         "groundling","opahs","epilator","slurries","ministry","flouncing","aggies","luteinizations","spinachlike","widowhood","koppies","et","consonantal","unwarped",
         "adhesion","gibberish","calamari","charts","straphanging","bewrap","mercs","damns","radiance","acyclovir","perikaryal","osteal","teniases","palomino",
         "qualmishly","deaminated","narcissistic","motivity","shirtwaist","dulcimore","prigged","libeller","detains","respading","vacuously","dozing","overdyer",
         "outgnaw","kraal","frontlist","mendelevium","connives","legibly","phoebe","play","misdrives","pigeonwing","telcos","barkers","mammee","holinesses","palpate",
         "overweighed","peonies","bequests","thoroughly","petrodollars","beanball","stints","roubles","chromatolyses","gollywog","proton","refurnish","ser","documental",
         "pleiotropy","treadlers","trusties","overthinks","aerodyne","fanciless","unhanging","oxidation","preformat","dogdom","multiheaded","liberalize","breezinesses",
         "solan","liquidity","waveoff","stateable","spinelle","bonhomous","pawky","phyle","borneols","mohurs","herbarium","craniocerebral","invalidisms","unbridles",
         "diuretically","imprecisenesses","surrounded","entitle","confusedness","decant","tarsal","yapons","conurbation","flavour","whaleman","barquentines",
         "triptych","doobie","snowbell","infamy","euphorbia","trammels","cantillated","cowberries","propulsions","gangstas","sustainability","pabulums",
         "cosmoline","zoogenic","husband","soloist","untidy","foxlike","drees","chestnuts","patina","inexplicability","subsense","simulating",
         "processibility","antalgic","counter","dosers","lucencies","antimicrobials","sand","adipocere","containerless","parises","depigmentation",
         "lithemias","modeled","reactivation","riled","subcompacts","camorra","dissociations","yager","pseudepigraphon","anybodies","losels",
         "parathyroid","inexpressibly","minxish","unroven","cautionary","dancing","countable","allowably","constructive","suedes","brag","orgasming",
         "melody","loopy","flourished","multitrillion","lee","taut","ferret","fribbles","baases","adenoid","counterplay","cowherb","tailoring","proverbial",
         "erythrons","trypanosomiasis","consorts","venturesomely","damndest","lividity","drowses","biographees","cockneyfying","regularize","uprighted",
         "chield","birdieing","shuckers","feverweed","obvert","beekeeping","constriction","wheeziest","nightcap","rewaken","denumerability","oncology",
         "screed","chases","sopite","embar","impossible","huipiles","haunch","saccharoidal","enthrone","freeloads","yeomanly","blackmailing","pipeless",
         "multiversities","mortices","filister","distaff","immediatenesses","hospitalizes","commonweal","seclusively","petulancies","proctors",
         "antiseparatists","interatomic","vatful","appreciates","spiderier","halites","unorthodoxies","marshinesses","pentamery","smartweed",
         "inappositeness","barretors","tempests","expressible","flatbread","antistrophes","pusillanimous","undernutrition","universals",
         "imposer","demean","domiciliations","overhigh","muezzins","aerobes","foy","superfarms","pathologically","gibbous","illuminating",
         "clubhauled","disciplinarity","statistic","penstemons","overdesigned","prilling","cockatoo","prefiguration","intagli",
         "scotopia","readjust","inwardness","astounds","tieback","fadeaways","snooted","turnstone","ghost","expellers",
         "overhope","donorships","boffo","scarify","flockier","subzones","predacious","excessiveness","glost","imputably",
         "flypaper","salesroom","applaudable","tableless","accept","floccose","slimpsiest","annunciated","angled","hilar","octonaries","kists"]

def get_word_from_api():

    try:
        url="https://random-word-api.herokuapp.com/word" 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        word=data[0]
        return word
    except requests.exceptions.RequestException:
        return None

def get_random_word():
    
    word=get_word_from_api()
    
    if word is None:
        return random.choice(WORDS)
    
    return word