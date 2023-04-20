from criteria import main
import argparse
import os

def parse_args():
	parser = argparse.ArgumentParser(description='Convert CidocCRM-based RDF to Mermaid')

	parser.add_argument("--diagramm_type", help='The type of the diagram', choices=['instance', 'ontology'])
	parser.add_argument("--folder", help='The source folder')
	parser.add_argument("--target_folder", help='Mermaid output folder')
	parser.add_argument("--file_type", help='The file extension to look in the source folder', choices=['turtle', 'ttl', 'rdfs'])
	
	args = parser.parse_args()
	return args

def process_folder(args): 
	files_in_folder = os.listdir(args.folder)
	filtered = filter(lambda file: file.split('.')[1] == args.file_type, files_in_folder)
	for file in filtered:
		file_name = file.split('.')[0]
		print(file_name)
		rdf = f'{args.folder}\\{file}'
		mmd = f'{args.target_folder}\\{file_name}.mmd'
		main(args.diagramm_type, rdf, mmd, None, 'config.json')

if __name__ == '__main__':
	args = parse_args()
	process_folder(args)
	#main(diagramm_type, args.rdf, args.mmd, args.shacl, args.configFile)