# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util,time

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.lastValue = util.Counter() # dict containing k-1 value for state
        self.policy = util.Counter()

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        #Value iteration is a method to calculate an optimal MDP policy and its value.

        startState = self.mdp.getStartState()

        #possibleActions = self.mdp.getPossibleActions(startState)
        #transitionStates = self.mdp.getTransitionStatesAndProbs(startState,possibleActions[0])
        allStates = self.mdp.getStates()
        allStates.reverse()

        terminalState = None
        canGoTerminal = None

        print "Start State ", startState
        #print "Possible actions of start state ",possibleActions
        #print "Transition states and probs from terminal state ",transitionStates
        #print "All the states are ",allStates
        #print "the reward from moving from start to next is ",reward

        for k in range(self.iterations):
            for state in allStates:
                tmpPolicy=None
                actionValues=util.Counter()

                possibleNextActions = self.mdp.getPossibleActions(state)
                for action in possibleNextActions:
                    possibleTransitions = self.mdp.getTransitionStatesAndProbs(state,action)
                    #print "The posssible action from ",state," is ",action," with transitions ",possibleTransitions
                    tmpValue=0
                    for transition in possibleTransitions:
                        thisReward = self.mdp.getReward(state, action, transition)
                        tmpValue+=transition[1]*(thisReward+self.discount*(self.values[transition[0]]))
                        #print "tmpValue is ",tmpValue
                        #print "Moving ",state," to ",transition[0]," with probability ", transition[1],"at iteration ",k,"gives tmpValue ",tmpValue," reward is ",thisReward
                        actionValues[action]=tmpValue

                self.values[state]=actionValues[actionValues.argMax()]
                tmpPolicy=actionValues.argMax()
                self.policy[state]=tmpPolicy


        #print "k value is ",k
        #for state in allStates:
            #print "the value for state ", state, " at iteration ",k-1," is ", self.values[state], " and the policy is ", self.policy[state]
            #print "the value for last state ", state, " at iteration ",k-1," is ", self.lastValue[state], " and the policy is ", self.policy[state]


    #for state in allStates:
        #print "the value for state ",state," is ",self.values[state]," and the policy is ",self.policy[state]




        time.sleep(0)






    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        return self.policy[state]

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
