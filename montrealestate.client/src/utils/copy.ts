export default function copy<T>(obj: T): T {
	return { ...obj };
}
