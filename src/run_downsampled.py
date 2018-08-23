from synorchestrator.orchestrator import set_queue_from_user_json, run_all

# An example script to be turned into a commandline script later.

# from synorchestrator.orchestrator import run_submission
# run_submission("Argon-Globus", "140814152850149946")

set_queue_from_user_json('tests/data/user_submission_example.json')
run_all()
