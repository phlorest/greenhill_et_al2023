import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill_et_al_subm"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'ua-covarion-relaxed.mcct.trees', detranslate=True),
            self.metadata,
            args.log)
        
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('ua-covarion-relaxed.trees.gz'),
                10001),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('utoaztecan.nex'),
            self.characters, 
            args.log)
