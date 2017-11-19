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


import mdp, util

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

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        print self.mdp.getStates()

        states=self.mdp.getStates()
        print "CONSTRUCTOR CALLED WITH ",self.iterations,' iterations '
        for k in range(self.iterations):
            newValues={}
            for state in states:
                actionValues=util.Counter()
                possibleActions=self.mdp.getPossibleActions(state)

                for action in possibleActions:
                    valueOfState=self.getQValue(state,action)
                    actionValues[action]=valueOfState
                maxValue=actionValues[actionValues.argMax()]
                newValues[state]=maxValue

            self.values=newValues




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
        qValue=0
        transitions=self.mdp.getTransitionStatesAndProbs(state,action)
        for transition in transitions:
            reward = self.mdp.getReward(state,action,transition[0])
            #print "the reward for the computed q value given state ",state," and action ",action," with transition ",transition," is reward :",reward
            qValue+=transition[1]*(reward+(self.discount*self.values[transition[0]]))
            #print "value from self.values [state]",self.values[transition[0]]," and the reward is ",reward

        #print "the q value for state ",state," with action ",action," is ",qValue
        return qValue
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
        #print "actions in this state are ",self.mdp.getPossibleActions(state)
        bestAction=None
        actions=util.Counter()
        for action in self.mdp.getPossibleActions(state):
            transitions = self.mdp.getTransitionStatesAndProbs(state,action)
            #print "Transitions for state ",state," with action ",action," are ",transitions
            value=0
            for transition in transitions:
                value+=transition[1]*(self.mdp.getReward(state,action,transition[0]) + self.discount * self.getValue(transition[0]))
                actions[action]=value
                #print "value for action ",action," from state ",state," to state ",transition[0]," is ",value

        #print 'best action for state ',state,' is ',actions.argMax()
        bestAction=actions.argMax()

        return bestAction
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
