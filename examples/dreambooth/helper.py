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
    }

    # configs = {
    #         "1": ["colorful cinematic still of " + token_name + " person with glasses, armor, cyberpunk,background made of brain cells, back light, organic, art by greg rutkowski, ultrarealistic, leica 30mm", num_step, guide, "rutkowski"],
    #         "2": ["pencil sketch of  " + token_name + " person inpired by greg rutkowski, digital art by artgem", num_step, guide, "rutkowskiartgem"],
    #         "3": ["photo, colorful cinematic still of  " + token_name + " person with glasses, organic armor, cyberpunk, background brain cells mesh, art by greg rutkowski", num_step, guide, "rutkowskibraincells"],
    #         "4": ["colorful cinematic still of " + token_name + " person with glasses, " + token_name + " person with long hair, color lights, on stage, ultrarealistic", num_step, guide, "longhair"],
    #         "5": ["photo, colorful cinematic still of  " + token_name + " person with organic armor, cyberpunk background,  " + token_name + " person, greg rutkowski", num_step, guide, "cyberpunkrutkowski"],
    #         "6": ["photo of  " + token_name + " person astronaut, astronaut, glasses, helmet in alien world abstract oil painting, greg rutkowski, detailed face", num_step, guide, "astronautrutkowski"],
    #         "7": ["photo of  " + token_name + " person as firefighter, helmet, ultrarealistic, leica 30mm", num_step, guide,  "firefighter"],
    #         "8": ["photo of  " + token_name + " person man as steampunk warrior, neon organic vines, glasses, digital painting", num_step, guide, "steampunk"],
    #         "9": ["impressionist painting of  " + token_name + " person by Daniel F Gerhartz, (( " + token_name + " person man with glasses painted in an impressionist style)), nature, trees", num_step, guide, "danielgerhartz"],
    # }
    if tests != "all":
        configs = { key: configs[key] for key in tests.split(",") }
    
    return configs
