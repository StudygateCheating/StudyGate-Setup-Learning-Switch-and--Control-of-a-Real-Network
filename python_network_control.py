
#Python networking

 mactable = {} 
 	#initialize operation dictionary
 	
 mactable[0x123] = 2
 	#append info to dictionsry
 	
  if 0x123 in mactable:
     print 'element 2 is in mactable'
 if 0x123 not in mactable:
     print 'element 2 is not in mactable'
     	#verify dictionary membership
     	
    	#POX debugging
 log.debug('saw new MAC!')
 log.error('unexpected packet causing system meltdown!')
 	#prints error msg in netwrok
 	
 out_action = of.ofp_action_output(port = of.OFPP_FLOOD)
 	#object communicates to packets
 	
 match = of.ofp_match()
 match.in_port = 3
 	#creates packets match
