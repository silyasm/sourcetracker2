# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class sourcetrackerV2:
    '''
    Module Name:
    sourcetrackerV2

    Module Description:
    A KBase module: sourcetrackerV2
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/silyasm/sourcetrackerV2"
    GIT_COMMIT_HASH = "49bb79a94fad0690caafc68f1bf96257a5a71edd"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_sourcetrackerV2(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_sourcetrackerV2
        #self.dfu = DataFileUtil(self.callback_url)
        alpha1 = .01
        alpha2 = .001
        beta = 10
        restarts = 5
        draws_per_restart = 1
        burnin = 2
        delay = 2
        #sources = pd.DataFrame[()]
        #sinks = pd.DataFrame[()]
        sample_type = params.get('sample_type')
        
        #amplicon_matrix, sample_types = get_df(params.get('associated_matrix_ref', self.dfu, sample_type)
        
        #for column in amplicon_matrix.columns:
        #    if sample_types.at[column, 0] == params.get('sink_label'):
        #        sink_column = amplicon_matrix.loc[:, column]
        #        sinks.insert(0, sink_column)
        #    if sample_types.at[column, 0] == params.get('source_label'):
        #        source_column = amplicon_matrix.loc[:, column]
        #        sources.insert(0, sink_column)
        #    else:
        #        raise.ValueError('The label' + column + 'does not match either sink nor source label')
        
        #mpm, mps, fas = gibbs(sources, sinks, alpha1, alpha2, beta, restarts, draws_per_restart, burnin, delay)
        
        
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[sample_type],
                                                'text_message': 'Yaya Toure'},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_sourcetrackerV2

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_sourcetrackerV2 return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
