FFEE (FaceFusion Enhanced Edition)
=================================

> Industry leading face manipulation platform.

![License](https://img.shields.io/badge/license-MIT-green)


Introduction
------------

FFEE (FaceFusion Enhanced Edition) is an improved version of the original FaceFusion platform, designed to provide a smoother and faster experience for users, especially those located in China. FFEE retains all the core functionalities of the original FaceFusion while introducing several key enhancements:

- **China Domestic CDN**: Faster access for users in China by serving assets through a domestic CDN, reducing latency and improving overall performance.
- **No NSFW Detection**: FFEE removes the NSFW detection feature, offering unrestricted usage across all content types.
- **Removal of Low-Quality Models**: We've cleaned up the model library by removing low-quality models, ensuring only the best and most reliable models are available for use.

Please note that the project structure, file names, and documentation remain consistent with the original FaceFusion project.


Preview
-------

![Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)


Installation
------------

Please refer to [installation](https://docs.facefusion.io/installation)


Usage
-----

Run the command:

```
python facefusion.py [commands] [options]

options:
  -h, --help                                      show this help message and exit
  -v, --version                                   show program's version number and exit

commands:
    run                                           run the program
    headless-run                                  run the program in headless mode
    force-download                                force automate downloads and exit
    job-list                                      list jobs by status
    job-create                                    create a drafted job
    job-submit                                    submit a drafted job to become a queued job
    job-submit-all                                submit all drafted jobs to become queued jobs
    job-delete                                    delete a drafted, queued, failed or completed job
    job-delete-all                                delete all drafted, queued, failed and completed jobs
    job-add-step                                  add a step to a drafted job
    job-remix-step                                remix a previous step from a drafted job
    job-insert-step                               insert a step to a drafted job
    job-remove-step                               remove a step from a drafted job
    job-run                                       run a queued job
    job-run-all                                   run all queued jobs
    job-retry                                     retry a failed job
    job-retry-all                                 retry all failed jobs
```


Documentation
-------------

For detailed documentation and advanced usage, please refer to the [original documentation](https://docs.facefusion.io). All documentation remains applicable to FFEE.
