# increasse the size of the micro_features
# Compare two variable simultaniously
# microFeature = np.random.randint(len(model -1))
# if ss[ hypo[i]+microFeature ] == model[microFeature] and ss[ hypo[i]+microFeature + 1 ] == model[microFeature - 1] :


import numpy as np

# search space (ss); target text (model); population size (N)
ss = ' try to find sds in this to sentence '
model = 'sentence'
N = 10
maxIter = 100

# INITIALISE AGENTS
hypo = np.random.randint(len(ss) - len(model)+ 2, size=(N));
status = np.zeros((N), dtype=bool)

for itr in range(maxIter):
    activeAgents = 0;
    # TEST PHASE
    for i in range(N):
        # PICK A MICROFEATURE TO PARTIALLY EVALUATE HYPOTHSIS
        # microFeature = np.random.randint(len(model))
        # microFeature2 = np.random.randint(len(model))
        # if ss[hypo[i] + microFeature] == model[microFeature] and ss[hypo[i] + microFeature2] == model[microFeature2]:
        # microFeature = np.random.randint(len(model)-1)
        # if ss[ hypo[i]+microFeature ] == model[microFeature] and ss[ hypo[i]+microFeature + 1 ] == model[microFeature - 1] :
        microFeature = np.random.randint(len(model))
        if ss[ hypo[i]+microFeature ] == model[microFeature]:
            status[i] = True
            activeAgents += 1
        else:
            status[i] = False

    # DIFFUSION PHASE
    for i in range(N):
        if status[i] == False:  # INACTIVE AGENT
            rand = np.random.randint(N)  # PICK RANDOM AGENT TO COMMUNICATE
            if status[rand] == True:  # SHARE HYPOTHESIS
                hypo[i] = hypo[rand];
            else:  # PICK A RANDOM HYPOTHSIS
                hypo[i] = np.random.randint(len(ss) - len(model))
        else:  # ACTIVE AGENT
            microFeature = np.random.randint(len(model))  # PICK MICROFEATURE
            if ss[hypo[i] + microFeature] == model[microFeature]:
                status[i] = True;
            else:
                status[i] = False;

    activityPercentage = activeAgents * 100 / N;
    # DISPLAYING ACTIVITY PERCENTAGE AND THE FIRST AGENT'S HYPOTHESIS
    print('Active agents:', activityPercentage, '%  ... found: ', ss[hypo[0]:hypo[0] + len(model)])
