import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill_et_al2023"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'ua-covarion-relaxed.mcct.trees', detranslate=True),
            self.metadata,
            args.log)

        posterior = self.raw_dir.read_trees(
            'ua-covarion-relaxed.trees.gz',
            burnin=10001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('utoaztecanKT.asc.nex'),
            self.characters, 
            args.log)
