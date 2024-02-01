from langchain.prompts import PromptTemplate


class PromptTranslationREADEME:
    def __init__(self, repo_url):
        self.repo_url = repo_url

    def _create_template(self):
        github_url = self.repo_url
        template = """해당 readme의 내용을 한글로 번역해서 markdown 파일 형태로 출력해줘 {github_url}"""

        return PromptTemplate(template=template, input_variables=["github_url"])
    def create(self):
        return self._create_template()

