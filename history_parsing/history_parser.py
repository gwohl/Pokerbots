#faded paper figures

'''
Parse history into a gigantic numpy array

[	
	(hand_num, bankroll_dict{}[player_name]), #head
	[not_dealer_id, not_dealer_post/fold {1,0}, dealer_, ...], #preflop
	[first_actor_id, first_actor_action1, other_action1, first_action2, ...], #flop
	[ _same_as_above_], #turn
	[ _same_as_above_ ], #river
	[winner_id, winning_total]  #results
] 


block_dict = 
{#dict
	str 'preflop':
		{#dict
			#str 'hand_header': (#tuple
								#int hand_num, 
								{#dict
									#str player_name1:bankroll1, 
									#str player_name2:bankroll2
								}
							)
		}
}



'''


class history_parser():

	def __init__(self, file_name):


		def parse_block(block):
			""""
			STATES
				0#preflop
				1#flop
				1.5#discard
				2#turn
				3#river
				4#results 
			"""

	 		game_states = ['preflop', 'flop', 'turn', 'river', 'results']


	 		preflop_dict = {}
	 		results = {}


			state = 'preflop' #init state
			lines = block.split("\n")

			win_seq = lines[len(lines)-1].split(" ")
			winning_dict = {win_seq[0]:int(win_seq[4][1:-1])}

			for i in range(len(lines)-1):
				line = lines[i]
				seq  = line.split(" ")



				if state == 'preflop':
					#print seq
					if line[:8] == '*** FLOP':
						state = 'flop'
						# for i in range(100):
						# 	print 'FLOP'
					else:
						if seq[0] == "Hand" and line[5] == '#':
							hand_num = int(seq[1][1:-1])

							#Finding bankrolls
							bankrolls = {seq[2]:int(seq[3][1:-2]), seq[4]:int(seq[5][1:-1])}

							hand_header = (hand_num, bankrolls)
							preflop_dict['hand_header'] = hand_header





						if seq[0] not in ['Dealt', 'Uncalled', 'Hand']: 
							if seq[1] not in ['posts', 'raises', 'wins', 'folds', 'checks', 'calls']:
								for i in range(10):
									print line

				if state == 'flop':
					print "here"
					if line[:8] == '*** TURN':
						state = 'turn'

				if state == 'turn':
					if line[:8] == '*** RIVER':
						state = 'river'

				if state == 'river':
					pass

			block_dict = {'preflop':preflop_dict, 'results':winning_dict}
			print block_dict

		self.raw_file = open(file_name)
		reading_file = self.raw_file.read()

		first_line_length = reading_file.find("\n")
		header = reading_file[:first_line_length].split(" ")
		self.player_1_name = header[4]
		self.player_2_name = header[6]

		self.stack_size = int(header[7][7:-1])
		self.big_blinds = int(header[8][3:-1])


		print "player 1: "+self.player_1_name
		print "player 2: "+self.player_2_name
		print "stack size: "+str(self.stack_size)
		print "big blinds: "+str(self.big_blinds)


		blocks = reading_file[first_line_length+1:].split("\n\n")

		print "===== GOING INTO THE BLOCKS ======"
		print ""
 		
 		
 		def testing(blocks):
			for i in range(len(blocks))[:1000]:
				parse_block( blocks[i] )
 			
 		def testing1(blocks):
			for i in range(len(blocks))[:10]:
				print "======="
				parse_block( blocks[i] )

		testing1(blocks)





h_p = history_parser('match_1.txt')