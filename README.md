# Workflow Orchestrator

| **Service \ Branch** | **master** | **develop** |
| -: | - | - |
| CI status | [![Travis-CI Build Status](https://travis-ci.org/Sage-Bionetworks/synapse-orchestrator.svg?branch=master)](https://travis-ci.org/Sage-Bionetworks/synapse-orchestrator) | [![Travis-CI Build Status](https://travis-ci.org/Sage-Bionetworks/synapse-orchestrator.svg?branch=develop)](https://travis-ci.org/Sage-Bionetworks/synapse-orchestrator) |
| Test coverage | [![Coverage Status](https://coveralls.io/repos/github/Sage-Bionetworks/synapse-orchestrator/badge.svg?branch=master)](https://coveralls.io/Sage-Bionetworks/synapse-orchestrator?branch=master) | [![Coverage Status](https://coveralls.io/repos/github/Sage-Bionetworks/synapse-orchestrator/badge.svg?branch=develop)](https://coveralls.io/Sage-Bionetworks/synapse-orchestrator?branch=develop) |
| Docs status | *pending* | *pending* |

This project coordinates workflows so that they can be queued, sent, and visualized in real-time across multiple WES endpoints/servers.

## Install and Run an Example

First, setup and install the following in a virtualenv:
```
virtualenv venv && . venv/bin/activate

git clone https://github.com/DataBiosphere/toil.git
cd toil
make prepare && make develop extras=[all]
cd ..

git clone https://github.com/ucsc-cgp/synapse-orchestrator.git
cd synapse-orchestrator
pip install . --process-dependency-links && pip install -r dev-requirements.txt
cd ..

git clone https://github.com/common-workflow-language/workflow-service.git
cd workflow-service
pip install . --process-dependency-links && pip install -r dev-requirements.txt
cd ..
```

Write a config at `~/orchestrator_config.json`, for example:
```
{
    "toolregistries": {
        "dockstore": {
            "host": "dockstore.org:8443", 
            "auth": "", 
            "proto": "https"
        }
    }, 
    "workflows": {
        "wdl_UoM_align": {
            "workflow_url": "tests/data/align.wdl", 
            "workflow_attachments": [], 
            "submission_type": "params", 
            "trs_id": "dockstore", 
            "version_id": "develop", 
            "workflow_type": "WDL"
        }
    }, 
    "workflowservices": {
        "local": {
            "host": "0.0.0.0:8080",
            "auth": {"Authorization": ""},
            "proto": "http",
            "wespath": "ga4gh/wes/v1/",
            "wfparam": "runs",
            "version": "1"
        }
    }
}
```

Then, activate the installation venv in 3 terminals:

Start the server in Terminal 1:
```(venv) $ wes-server --backend=wes_service.toil_wes --opt extra=--clean=never```

Load the orchestrator monitor in Terminal 2:
```(venv) $ orchestrate```

In Terminal 3, an example use case might be to write a small script like:
```
from synorchestrator.orchestrator import set_queue_from_user_json, run_all

set_queue_from_user_json('tests/data/user_submission_example.json')
run_all()
```
 
 And run it:
```(venv) $ python run_script.py```
