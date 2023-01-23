import ipywidgets as widgets

class FormCreator:
    def __init__(self):
        '''
        self.software_md_section()
        self.discoverability_section()
        self.dev_community_section()
        self.runtime_section()
        self.current_version_section()
        self.additional_info_section()
        self.authors_section()
        self.setup_generate_yaml()
        '''
        layout = widgets.Layout(width="auto", height="40px")
        style = {'description_width' : 'initial'}

        self.base_args = { 'layout' : layout, 'style' : style }

    ## SOFTWARE METADATA
    def software_md_section(self):
        # name; software titlejupy
        self.name = widgets.Text(placeholder="My Software", title="Software Title", description="the software title", **self.base_args)

        # description
        self.desc = widgets.Text(placeholder="My Software does this and that!", **self.base_args)

        # creation date; YYYY-MM-DD
        self.creation_date = widgets.DatePicker(description="YYYY-MM-DD", **self.base_args)

        # first release date; YYYY-MM-DD
        self.f_release_date = widgets.DatePicker(description="YYYY-MM-DD", **self.base_args)

        # license
        self.license = widgets.Text(description="from SPDX license list", **self.base_args)

        display(self.name, self.desc, self.creation_date, self.f_release_date, self.license)

    ## DISCOVERABILITY & CITATION
    def discoverability_section(self):
        # unique identifier
        self.id = widgets.Text(placeholder="10.151.xxxxx", description="e.g. ISBN, GTIN, UUID", **self.base_args)

        # application category
        self.category = widgets.Text(placeholder="Astronomy", **self.base_args)

        # keywords
        # separate multiple keywords by comma
        self.keywords = widgets.Text(placeholder="ephemerides, orbit, astronomy", **self.base_args)
        # list(map(str, input().split(',')))

        # funding 
        self.funding = widgets.Text(placeholder="PRA_2018_73", description="grant funding software development", **self.base_args)

        # funder
        self.funder = widgets.Text(placeholder="Universita di Pisa", description="organization funding software development", **self.base_args)

        display(self.id, self.category, self.keywords, self.funding, self.funder)

    ## DEVELOPMENT COMMUNITY TOOLS
    def dev_community_section(self):
        # code repo
        self.repo = widgets.Text(placeholder="git+https://github.com/you/reponame.git", **self.base_args)

        # continuous integration
        self.ci = widgets.Text(placeholder="https://travis-ci.org/you/reponame", **self.base_args)

        # issue tracker
        self.issues = widgets.Text(placeholder="https://github.com/you/reponame.git/issues", **self.base_args)

        # related links
        self.related_links = widgets.Text(**self.base_args)

        display(self.repo, self.ci, self.issues, self.related_links)

    ## RUN-TIME ENVIRONMENT
    def runtime_section(self):
        # Programming language
        self.p_lang = widgets.Text(placeholder="C#, Java, Python 3", **self.base_args)

        # runtime platform
        self.runtime_plat = widgets.Text(placeholder=".NET, ...", **self.base_args)

        # operating system
        self.os = widgets.Text(placeholder="Linux, MacOS, Windows", **self.base_args)

        # other software requirements
        self.requirements = widgets.Text(**self.base_args)

        display(self.p_lang, self.runtime_plat, self.os, self.requirements)

    ## CURRENT VERSION OF THE SOFTWARE
    def current_version_section(self):
        # version number 
        self.ver_no = widgets.Text(placeholder="1.0.0", **self.base_args)

        # release date
        self.release_date = widgets.DatePicker(description="YYYY-MM-DD", **self.base_args)

        # download url
        self.download_url = widgets.Text(placeholder="https://example.org/MySoftware.tar.gz", **self.base_args)

        # release notes
        self.release_notes = widgets.Text(placeholder="Change log: this and that; Bugfixed: that and this.", **self.base_args)

        display(self.ver_no, self.release_date, self.download_url, self.release_notes)

    ## ADDITIONAL INFO
    def additional_info_section(self):
        # Reference publication
        self.ref_pub = widgets.Text(placeholder="https://doi.org/10.1000/xyz123", **self.base_args)

        # Development status
        self.dev_status = widgets.Text(description="see www.repostatus.org for details", **self.base_args)

        # is part of
        self.part_of = widgets.Text(placeholder="https://the.bigger.framework.org", **self.base_args)

        display(self.ref_pub, self.dev_status, self.part_of)

    def authors_section(self):
        ## AUTHORS
        self.authors = []

        # Given Name
        self.f_name = widgets.Text(placeholder="John", **self.base_args)

        # family name
        self.l_name = widgets.Text(placeholder="Doe", **self.base_args)

        # email adress
        self.email = widgets.Text(placeholder="j.doe@example.org", **self.base_args)

        # URI
        self.uri = widgets.Text(placeholder="http://orcid.org/0000-0002-1825-0097", **self.base_args)

        # Affiliation
        self.affiliation = widgets.Text(placeholder="Department of Computer Science, University of Pisa", **self.base_args)

        display(self.f_name, self.l_name, self.email, self.uri, self.affiliation)

    ## EXPORT TO YAML
    def input_to_yaml(self):
        # create dict
        spec = { "openapi" : "3.0.0" }

        # fill info with input
        sinfo = {}

        sinfo["title"] = self.name
        sinfo["version"] = str(self.ver_no)
        sinfo["description"] = self.desc
        sinfo["contact"] = { "name" : self.authors[0][0] + " " + self.authors[0][1], 
                            "email" : self.authors[0][2],
                            "url" : self.authors[0][3],
                            "x-affiliation" : self.authors[0][4] }
        sinfo["license"] = { "name" : license }
        sinfo["x-created"] = str(self.creation_date)
        sinfo["x-first-release"] = str(self.f_release_date)
        sinfo["x-programming-lang"] = self.p_lang
        sinfo["x-platform"] = self.runtime_plat
        sinfo["x-os"] = self.os
        sinfo["x-id"] = str(id)
        sinfo["x-category"] = self.category
        sinfo["x-keywords"] = ','.join(self.keywords)
        sinfo["x-funding"] = str(self.funding)
        sinfo["x-funder"] = str(self.funder)
        sinfo["x-repository"] = str(self.repo)
        sinfo["x-ci"] = str(self.ci)
        sinfo["x-issue-tracker"] = str(self.issues)
        sinfo["x-related-links"] = str(self.related_links)
        sinfo["x-version-release"] = str(self.release_date)
        sinfo["x-download-url"] = str(self.download_url)
        sinfo["x-release-notes"] = str(self.release_notes)
        sinfo["x-reference-pub"] = str(self.ref_pub)
        sinfo["x-dev-status"] = str(self.dev_status)
        sinfo["x-part-of"] = str(self.part_of)

        sinfo = {key : val for key, val in sinfo.items() if (val is not None and val != '')}

        spec["info"] = sinfo

        import yaml
        with open('meta.yaml', 'w+') as f:
            yaml.dump(spec, f, allow_unicode=True)

    def on_button_clicked(self, b):
            self.input_to_yaml()
            with self.output:
                print("meta.yaml generated")

    def setup_generate_yaml(self):
        ## DISPLAY BUTTON
        self.button = widgets.Button(description="Generate meta.yaml")
        self.output = widgets.Output()

        display(self.button, self.output)
            
        self.button.on_click(self.on_button_clicked)
