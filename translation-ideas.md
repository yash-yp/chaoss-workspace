
# Guidelines for Translation of Metrics

This page provides the guidelines in regard to the process of translating metrics into other various languages.

## Adding translations in a new language

- Before adding translations in a new language, it is strongly recommended to have an active community of native speakers of that language.
- To begin with, create a new directory in the [translations repository](). Name the directory as the language in which the metrics are to be translated.
- Create subdirectories for each working group within the language directory. Note that the name of the sub-directories must match with the repository names of the working groups. (e.g - wg-common, wg-value etc.)
- The structure of the subdirectory for each working group should be the same as specified for the working group repositories on this [page](https://handbook.chaoss.community/community-handbook/community-initiatives/working-groups/wg-repository-structure). Note:- The base files can be ignored except for the README.
- Follow the templates of other files analogous to as specified in the [governance repository](https://github.com/chaoss/governance/tree/master/templates) 
- The metrics themselves also follow a [standard template](https://github.com/chaoss/metrics/blob/master/resources/metrics-template.md)It is recommended to create a translated version of this template. 
- Further, the directories and the files must be named in English only.
- The directory structure for translations in a new language is now ready. The translated metrics can be added depending upon their respective working group and the focus area.
- The above steps should be completed by the translating community before starting with the translation of the metrics.

## Updating translations

- The working groups keep revising the focus areas and the metrics regularly. Therefore, it is necessary for the translations to be updated as per the current version of the release. Following steps are helpful to ensure this:
- There are four possible events that involve the translations community. These are when:
  - A new metric is released
  - A focus area or metric is renamed
  - An existing metric is updated
  - An existing metric is removed
- In any of the above scenarios, the label - “needs translation attention” must be added to the relevant issue or pull request. This step should be ensured by the contributors/ reviewers of the issue/ pull request.
- The team for the translations can also be mentioned in this issue/ PR.
- Once the issue/PR is closed/merged, the contributors/reviewers must open a new issue in the translations repository linking to the original change.
- The relevant commit hash and message can also be provided so that the changes are easily located via the `git diff` command.
- The translation community should then investigate the issue and try to accommodate the changes in the translated metrics. 
- When the change is implemented in all translated languages, the issue may be closed.

## Other information

- The English version of the metrics is original and must be used as the only source during the translation process.
- Presently, the [templates]() are maintained only in English. These templates can be translated into different languages as and when required to ensure consistency among the translations.
- Follow the general conventions related to naming and structure as specified [here](https://handbook.chaoss.community/community-handbook/community-initiatives/working-groups/wg-repository-structure#general-conventions)
