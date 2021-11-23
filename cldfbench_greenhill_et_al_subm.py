import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill_et_al_subm"

    def cmd_makecldf(self, args):
        self.init(args)

        with phlorest.NexusFile(self.cldf_dir / 'summary.trees') as nex:
           self.add_tree_from_nexus(
               args,
               self.raw_dir / 'ua-covarion-relaxed.mcct.trees',
               nex,
               'summary',
               'summary',
               detranslate=True,
           )

        posterior = self.sample(
           self.remove_burnin(
               self.read_gzipped_text(self.raw_dir / 'ua-covarion-relaxed.trees.gz'),
               10001),
           detranslate=True,
           as_nexus=True)

        with phlorest.NexusFile(self.cldf_dir / 'posterior.trees') as nex:
           for i, tree in enumerate(posterior.trees.trees, start=1):
               self.add_tree(args, tree, nex, 'posterior-{}'.format(i), 'sample')

        self.add_data(args, self.raw_dir / 'utoaztecan.nex')
