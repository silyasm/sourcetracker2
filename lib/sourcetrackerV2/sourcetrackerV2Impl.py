# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from sourcetrackerV2.util import _sourceTrackerUtil
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
    GIT_COMMIT_HASH = "d5c2bd63cc221cd5d8a1895a4e957d7f0abd5c73"

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
        # example source otus
        otus = np.array(['o%s' % i for i in range(50)])
        source1 = np.random.randint(0, 1000, size=50)
        source2 = np.random.randint(0, 1000, size=50)
        source3 = np.random.randint(0, 1000, size=50)
        source_df = pd.DataFrame([source1, source2, source3], index=['source1', 'source2', 'source3'], columns=otus, dtype=np.int32)
        
        # example sink otus
        sink1 = np.ceil(.5*source1+.5*source2)
        sink2 = np.ceil(.5*source2+.5*source3)
        sink3 = np.ceil(.5*source1+.5*source3)
        sink4 = source1
        sink5 = source2
        sink6 = np.random.randint(0, 1000, size=50)
        sink_df = pd.DataFrame([sink1, sink2, sink3, sink4, sink5, sink6], index=np.array(['sink%s' % i for i in range(1,7)]), columns=otus, dtype=np.int32)
        
        alpha1 = .01
        alpha2 = .001
        beta = 10
        restarts = 5
        draws_per_restart = 1
        burnin = 2
        delay = 2
        
        mpm, mps, fas = _sourceTrackerUtil.gibbs((source_df, sink_df, alpha1, alpha2, beta, restarts, draws_per_restart, burnin, delay, create_feature_tables=True)
        
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': 'Proportion Tables'},
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
