def dummy(images, **kwargs):
    return images, False

def create_tests(tests, token_name, num_step, guide):
    configs = {
            "1": ["colorful cinematic still of " + token_name + " person, armor, cyberpunk,background made of brain cells, back light, organic, art by greg rutkowski, ultrarealistic, leica 30mm", num_step, guide, "rutkowski"],
            "2": ["pencil sketch of  " + token_name + " person inpired by greg rutkowski, digital art by artgem", num_step, guide, "rutkowskiartgem"],
            "3": ["photo, colorful cinematic still of  " + token_name + " person, organic armor, cyberpunk, background brain cells mesh, art by greg rutkowski", num_step, guide, "rutkowskibraincells"],
            "4": ["colorful cinematic still of " + token_name + " person, " + token_name + " person with long hair, color lights, on stage, ultrarealistic", num_step, guide, "longhair"],
            "5": ["photo, colorful cinematic still of  " + token_name + " person with organic armor, cyberpunk background,  " + token_name + " person, greg rutkowski", num_step, guide, "cyberpunkrutkowski"],
            "6": ["photo of  " + token_name + " person astronaut, astronaut, helmet in alien world abstract oil painting, greg rutkowski, detailed face", num_step, guide, "astronautrutkowski"],
            "7": ["photo of  " + token_name + " person as firefighter, helmet, ultrarealistic, leica 30mm", num_step, guide,  "firefighter"],
            "8": ["photo of  " + token_name + " person as steampunk warrior, neon organic vines, digital painting", num_step, guide, "steampunk"],
            "9": ["impressionist painting of  " + token_name + " person by Daniel F Gerhartz, (( " + token_name + " person with painted in an impressionist style)), nature, trees", num_step, guide, "danielgerhartz"],
        #    "10": ["A digital painting of " + token_name + " person from Metal Gear Solid, Yoji Shinkawa", num_step, guide, "mgs"],
        #    "11": ["Movie still of " + token_name + " person as Doctor Strange.", num_step, guide, "drstrange"],
        #    "12": ["Movie still of " + token_name + " person as Maverick from Top Gun.", num_step, guide, "topgun"],
        #    "13": ["Movie still of " + token_name + " person from a 007 movie.", num_step, guide, "007"],
        #    "14": ["Movie still of " + token_name + " person as Indiana Jones.", num_step, guide, "indianajones"],
        #    "15": ["Movie still of " + token_name + " person as a Jedi from Star Wars.", num_step, guide, "jedi"],
        #    "16": ["colorful portrait of " + token_name + " person with dark glasses as eminem, gold chain necklace, relfective puffer jacket, short white hair, in front of music shop, ultrarealistic, leica 30mm", num_step, guide, "eminem"],
        #    "17": ["colorful photo of  " + token_name + " person as kurt cobain with glasses, on stage, lights, ultrarealistic, leica 30mm", num_step, guide, "kurtcobain"],
        #    "18": ["photo of  " + token_name + " person as serious spiderman with glasses, ultrarealistic, leica 30mm", num_step, guide, "spiderman"],
        #    "19": ["photo of  " + token_name + " person man as supermario with glassesm mustach, blue overall, red short, " + token_name + " person. ultrarealistic, leica 30mm", num_step, guide, "supermario"],
        #    "20": ["photo of  " + token_name + " person as targaryen warrior with glasses, long white hair, armor, ultrarealistic, leica 30mm", num_step, guide, "targaryen"],
        #    "21": ["photo of  " + token_name + " person as man with glasses, bowler hat, in django unchained movie, ultrarealistic, leica 30mm", num_step, guide, "django"],
    }

    if tests != "all":
        configs = { key: configs[key] for key in tests.split(",") }
    
    return configs