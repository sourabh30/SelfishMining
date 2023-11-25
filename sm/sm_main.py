from sm_strategy import SelfishMining
from learning_automata_type import LearningAutomataType

iteration_number = 10000

tow_number = 10
min_tow_block_number = 4
max_tow_block_number = 6

selfish_mining = SelfishMining(
    tow_number, min_tow_block_number, max_tow_block_number, 0.01, 0.01, 1, 3, LearningAutomataType.AVDHLA, False)
selfish_mining.alpha = 0.45
selfish_mining.gamma = 0.5
# selfish_mining.print_input_statistic()

selfish_mining.start_simulate(iteration_number)
selfish_mining.print_final_result()

selfish_mining.visualize_data(iteration_number)
